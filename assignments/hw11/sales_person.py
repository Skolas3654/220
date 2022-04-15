class SalesPerson:
    def __init__(self,employee_id,name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        sale_sum = 0
        for i in self.sales:
            sale_sum += i
        return sale_sum

    def get_sales(self):
        return self.sales

    def met_quota(self,quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        other_sales = other.total_sales()
        if self.total_sales() == other_sales:
            return 0
        elif self.total_sales() > other_sales:
            return 1
        else:
            return -1

    def __str__(self):
        group = str(self.get_id()),self.name,str(self.total_sales())
        group = list(group)
        group.insert(1,'-')
        group.insert(3, ': ')
        group = "".join(group)
        return group
