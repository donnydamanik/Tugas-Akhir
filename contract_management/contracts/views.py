from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.timezone import now
from datetime import timedelta
from .models import Contract
from .forms import ContractForm

def contract_list(request):
    
    today = now().date()

    urgent_contracts = Contract.objects.filter(end_date__lte=today + timedelta(days=7))
    upcoming_contracts = Contract.objects.filter(end_date__lte=today + timedelta(days=30)).exclude(id__in=urgent_contracts)

    
    all_contracts = Contract.objects.all()

    context = {
        'urgent_contracts': urgent_contracts,     
        'upcoming_contracts': upcoming_contracts, 
        'contracts': all_contracts,
    }
    return render(request, 'contracts/contract_list.html', context)

def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contract added successfully.')
            return redirect('contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts/contract_form.html', {'form': form})

def contract_update(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contract updated successfully.')
            return redirect('contract_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/contract_form.html', {'form': form})

def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        messages.success(request, 'Contract deleted successfully.')
        return redirect('contract_list')
    return render(request, 'contracts/contract_confirm_delete.html', {'contract': contract})
