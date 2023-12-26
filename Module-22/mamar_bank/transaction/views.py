from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView
from .models import Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DepositForm,WithdrawForm,LoanRequestForm
from .constants import DEPOSIT,WITHDRAWAL,LOAN,LOAN_PAID
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
from django.views import View
from django.urls import reverse_lazy
# Create your views here.

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name='transcation/transaction_form.html'
    model=Transaction
    title=''
    success_url=reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
        })
        return context
    
class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self) :
        initial={'transaction_type': DEPOSIT }
        return initial
    def form_valid(self, form):
        amount=form.cleaned_data['amount']
        account=self.request.user.account
        account.balance+=amount
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request,f'{amount}$ deposited successfully')
        return super().form_valid(form)
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class=WithdrawForm
    title='Withdraw'

    def get_initial(self):
        initial={'transaction_type': WITHDRAWAL}
        return initial
    def form_valid(self, form):
        amount=form.cleaned_data['amount']
        account=self.request.user.account
        account.balance-=amount
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request,f'{amount}$ withdraw successfully')
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_class=LoanRequestForm
    title='Request For Loan'

    def get_initial(self):
        initial={'transaction_type': LOAN}
        return initial
    def form_valid(self, form):
        amount=form.cleaned_data['amount']
        loan_request_count=Transaction.objects.filter(account=self.request.user.account, transaction_type=3,loan_approved=True).count()
        if loan_request_count>=3:
            return HttpResponse('You Have crossed your limits')
        messages.success(self.request,f'{amount}$ for loan request is submitted wait for admin')
        return super().form_valid(form)
    
class TransactionReportView(ListView):
    template_name='transcation/transaction_report.html'
    model=Transaction
    balance=0
    
    def get_queryset(self):
        queryset=super().get_queryset().filter(
            account=self.request.user.account
        )

        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()  # Fix the format here
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance=queryset.filter(
                timestamp__date__gte=start_date,timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']

        else:
            self.balance=self.request.user.account.balance

        return queryset.distinct()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })
        return context
    

class PayLoanView(LoginRequiredMixin,View):
    def get(self, request, loan_id):
        loan=get_object_or_404(Transaction,id=loan_id)

        if loan.loan_approved:
            user_account=loan.account

            if loan.amount<user_account.amount:
                user_account.amount-=loan.amount
                loan.balance_after_transaction=user_account.balance
                user_account.save()
                loan.transaction_type=LOAN_PAID
                loan.save()
                return redirect('')
            else:
                messages.error(self.request,f'Loan amount is greater than your available balance')
                return redirect('transaction_report')

class LoanListView(LoginRequiredMixin,ListView):
    template_name = 'transaction/loan_request.html'
    model = Transaction
    context_object_name = 'loans' # loan list ta ei loans context er moddhe thakbe
    
    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account=user_account,transaction_type=3)

        return queryset

