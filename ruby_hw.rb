require "csv"

    
    vms_csv = CSV.read("./02_ruby_vms.csv", converters: :numeric)
    volumes_csv = CSV.read("./02_ruby_volumes.csv", converters: :numeric)
    prices_csv = CSV.read("./02_ruby_prices.csv", converters: :numeric).to_h

class VirtualMachine
    attr_accessor :id, :cpu, :ram, :hdd_type, :hdd_capacity, :additional_hdds
        def initialize(vms) 
          @id = vms[0]
          @cpu = vms[1]
          @ram = vms[2]
          @hdd_type = vms[3]
          @hdd_capacity = vms[4]
          @additional_hdds = []
        end
  
        def add_hdd(hdd) 
          @additional_hdds << hdd
        end
end

class CreateData
  class << self

    attr_reader :vms, :volumes, :prices

    def create_data(vms, volumes, prices)
    @vms = vms
    @volumes = volumes
    @prices = prices
    create_vm
    end

    def create_vm
      @vms.map! do |vm|
        vm
        new_vm = VirtualMachine.new(vm)
        new_vm.add_hdd(volumes.select { |vol| vol[0] == vm[0] }) 
        new_vm.additional_hdds = new_vm.additional_hdds.flatten(1) 
        new_vm 
      end
    end

  end
end

class Report
  
  attr_accessor :costs

  def initialize(vms, prices)
    @vms = vms
    @prices = prices
    calc_the_costs_of_vms
  end
 
  def calc_the_costs_of_vms
      costs = []
      add_cost = 0
      @vms.each do |vm|
        cost = (vm.cpu * @prices['cpu'] + vm.ram * @prices['ram'] + vm.hdd_capacity * @prices["#{vm.hdd_type}"])/100
        costs << [vm.id, cost]
        unless vm.additional_hdds.empty?
          vm.additional_hdds.each { |vol| add_cost += vol[2] * @prices["#{vol[1]}"] }
          add_cost = add_cost/100
          costs[vm.id][1] += add_cost
        end       
      end
    costs = costs.sort_by! { |x| x[1] }
  end

  def most_expencive(n)
    calc_the_costs_of_vms.last(n)
  end

  def less_expencive(n)
    calc_the_costs_of_vms.reverse.last(n)
  end

  def largest_vm_by_capacity (n, hdd_type)
    all_capacities = []
    @vms.each do |vm|
      capacity = 0
      vm.additional_hdds.each do |volume|
        if volume[1] == hdd_type
          capacity += volume[2]
        end
      end
      if vm.hdd_type == hdd_type
        capacity += vm.hdd_capacity  
      end
      all_capacities << [vm.id, capacity]
      all_capacities = all_capacities.sort_by! { |x| x[1] }
    end
    all_capacities.last(n)
  end

  def mvs_with_the_largest_number_of_volumes_depending_on_hdd_type(n, hdd_type = nil)
    hdds = []
#    case hdd_type
#      when nil    
      @vms.each do |vm| 
        if hdd_type
          hdds_of_a_specific_type = vm.additional_hdds.select { |vol|  vol[1] == hdd_type }
          hdds << [vm.id, hdds_of_a_specific_type.size]
        else
          hdds << [vm.id, vm.additional_hdds.size]
        end
      end
    hdds = hdds.sort_by! { |x| x[1] } 
    hdds.last(n) 
  end

  def mvs_with_the_largest_capacity_of_volumes_depending_on_hdd_type(n, hdd_type = nil)
    hdds = [] 
    @vms.each do |vm|
      capacity = 0 
      unless hdd_type
        vm.additional_hdds.each { |volume| capacity += volume[2] }
        hdds << [vm.id, capacity]
      else
        vm.additional_hdds.each do |volume|
          if volume[1] == hdd_type
            capacity += volume[2]
          end
        end
        hdds << [vm.id, capacity]
      end 
  end
  hdds = hdds.sort_by! { |x| x[1] } 
  hdds.last(n)
end

end

CreateData.create_data(vms_csv, volumes_csv, prices_csv)

report = Report.new(CreateData.vms, CreateData.prices)

 p report1 = report.most_expencive(ARGV[0].to_i)
 p report2 = report.less_expencive(ARGV[0].to_i)
 p report3 = report.largest_vm_by_capacity(ARGV[0].to_i, "sata")
 p report4 = report.mvs_with_the_largest_number_of_volumes_depending_on_hdd_type(ARGV[0].to_i)
 p report5 = report.mvs_with_the_largest_capacity_of_volumes_depending_on_hdd_type(ARGV[0].to_i)

