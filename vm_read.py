import csv


with open('02_ruby_vms.csv') as f:
    vms_csv = list(csv.reader(f))
    #print(vms_csv)

with open('02_ruby_prices.csv') as f:
    vms_prices = dict(csv.reader(f))
    #print(vms_prices)
        
with open('02_ruby_volumes.csv') as f:
    vms_volumes = list(csv.reader(f))
    #print(vms_volumes)



class VirtualMachine:

	
	def __init__(self, id, ram, cpu, hdd_type, hdd_capacity, add_hdds):
		self.id = id
		self.ram = ram 
		self.cpu = cpu
		self.hdd_type = hdd_type
		self.hdd_capacity = hdd_capacity
		self.add_hdds = []

def create_vm(vm):
	new_vm = VirtualMachine (
		id = vm[0],
		ram =  vm[1],
    	cpu = vm[2],
    	hdd_type = vm[3],
    	hdd_capacity = vm[4],
		add_hdds = [])	

for vm in vms_csv:
	create_vm(vm)

class AdditionalHdd:

	
	def __init__(self, vm_id, hdd_type, hdd_capacity):
		self.vm_id = vm_id
		self.hdd_type = hdd_type
		self.hdd_capacity = hdd_capacity

def create_hdd(hdd):
	new_hdd = AdditionalHdd (
		vm_id = hdd[0],
    	hdd_type = hdd[1],
    	hdd_capacity = hdd[2])

print(vms_csv[0])

for hdd in vms_volumes:
	create_hdd(hdd)