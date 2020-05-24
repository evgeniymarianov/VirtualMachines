import csv
from functools import reduce


with open('vms.csv') as f:
    vms_csv = list(csv.reader(f))
    #print(vms_csv)

with open('prices.csv') as f:
    prices = dict(csv.reader(f))

for key, value in prices.items():
    if key in ['cpu', 'ram', 'hdd_capacity', 'ssd', 'sata', 'sas']:
        prices[key] = int(value)
        
with open('volumes.csv') as f:
    vms_volumes = list(csv.reader(f))
    #print(vms_volumes)



class VirtualMachine:

	
	def set(self, id, ram, cpu, hdd_type, hdd_capacity, add_hdds):
		self.id = int(id)
		self.ram = int(ram)
		self.cpu = int(cpu)
		self.hdd_type = hdd_type
		self.hdd_capacity = int(hdd_capacity)
		self.add_hdds = add_hdds
		self.cost = (cpu * prices['cpu'] + ram * prices['ram'] + hdd_capacity * prices[hdd_type] + sum(list(map(lambda hdd: hdd.cost, add_hdds)))) * 0.01

class AdditionalHdd:

	
	def set(self, vm_id, hdd_type, hdd_capacity):
		self.vm_id = int(vm_id)
		self.hdd_type = hdd_type
		self.hdd_capacity = int(hdd_capacity)
		self.cost = int(hdd_capacity) * prices[hdd_type]

AddHdds = []
for hdd in vms_volumes:
	new_hdd = AdditionalHdd ()
	new_hdd.set (hdd[0], hdd[1], hdd[2])
	AddHdds.append(new_hdd)

VMs = []
for vm in vms_csv:
	#print(vm)
	new_vm = VirtualMachine ()
	#print(list(filter(lambda hdd: hdd.vm_id == int(vm[0]), AddHdds)))
	new_vm.set (int(vm[0]), int(vm[1]), int(vm[2]), vm[3], int(vm[4]), list(filter(lambda hdd: hdd.vm_id == int(vm[0]), AddHdds)))
	VMs.append(new_vm)

VMs = sorted(VMs, key=lambda vm: vm.cost)

def most_expensive(number):
	short = VMs[:number]
	report = []
	for vm in short:
		report.append([str(vm.id), round((vm.cost), 2)])
	print(report)

def most_cheapest(number):
	short = VMs[len(VMs) - number:]
	report = []
	for vm in short:
		report.append([str(vm.id), round((vm.cost), 2)])
	print(report)

def most_voluminous(number, type):
	report = []
	for vm in VMs:
		same_volume = 0
		if vm.hdd_type == type:
		    same_volume += vm.hdd_capacity
		if len(vm.add_hdds) > 0:
			for hdd in vm.add_hdds:
				if hdd.hdd_type == type:
					same_volume += hdd.hdd_capacity
		report.append([str(vm.id), same_volume])
	report.sort(key=lambda i: i[1])
	print(report[len(VMs) - number:])

def largest_number_of_hdds_by_type(number, *args):
	type = args[0]
	report = []
	for vm in VMs:
		same_hdds = 0
		if type:
			if len(vm.add_hdds) > 0:
			    for hdd in vm.add_hdds:
				    if hdd.hdd_type == type:
					    same_hdds += 1
		for hdd in vm.add_hdds:
			same_hdds += 1
		report.append([str(vm.id), same_hdds])
	report.sort(key=lambda i: i[1])
	print(report[len(VMs) - number:])

def largest_number_of_hdds_by_capacity(number, *args):
	type = args[0]
	report = []
	for vm in VMs:
		same_volume = 0
		if type:
			if len(vm.add_hdds) > 0:
			    for hdd in vm.add_hdds:
				    if hdd.hdd_type == type:
					    same_volume += hdd.hdd_capacity
						#print('hdd.hdd_capacity = ' + str(hdd.hdd_capacity) + 'same_volume = ' + str(same_volume))
		for hdd in vm.add_hdds:
			same_volume += hdd.hdd_capacity
		report.append([str(vm.id), same_volume])
	report.sort(key=lambda i: i[1])
	print(report[len(VMs) - number:])



#reduce(lambda x, y: x + y, list(filter(lambda hdd: hdd.hdd_type == some_type, vm.add_hdds)))
most_expensive(10)
most_cheapest(10)
most_voluminous(10, 'sata')
largest_number_of_hdds_by_type(10, 'sata')
largest_number_of_hdds_by_capacity(10, 'sata')

