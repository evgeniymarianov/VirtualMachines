import csv
from functools import reduce


with open('02_ruby_vms.csv') as f:
    vms_csv = list(csv.reader(f))
    #print(vms_csv)

with open('02_ruby_prices.csv') as f:
    prices = dict(csv.reader(f))

for key, value in prices.items():
    if key in ['cpu', 'ram', 'hdd_capacity', 'ssd', 'sata', 'sas']:
        prices[key] = int(value)
print(prices)
        
with open('02_ruby_volumes.csv') as f:
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
	print(new_vm.cost)






