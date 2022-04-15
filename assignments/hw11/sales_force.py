from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self,file_name):
        file = open(file_name, 'r')
        for line in file:
            split_list = line.split()
            emp_id = int(split_list[0].replace(",",''))

            name = split_list[1:3]
            name = " ".join(name).replace(",",'')

            sales = split_list[3:len(split_list)]
            sales_p = SalesPerson(emp_id, name)
            for i in sales:
                sale = float(i)
                sales_p.enter_sale(sale)

            self.sales_people.append(sales_p)


    def quota_report(self,quota):
        full_list = []
        for emp in self.sales_people:
            one_list = []

            emp_id = emp.get_id()
            name = emp.get_name()
            total = emp.total_sales()

            one_list.append(emp_id)
            one_list.append(name)

            one_list.append(total)
            if total >= quota:
                one_list.append(True)
            else:
                one_list.append(False)
            full_list.append(one_list)
        return full_list


    def top_seller(self):
        sales_list = []
        top_seller = []
        for i in self.sales_people:
            sales_list.append(i.total_sales())
        max_sale = max(sales_list)
        if sales_list.count(max_sale) > 1:
            index = sales_list.index(max_sale)
            top_seller.append(self.sales_people[index])
            top_seller.append(self.sales_people[index+1])
        else:
            index = sales_list.index(max_sale)
            top_seller.append(self.sales_people[index])
        return top_seller


    def individual_sales(self,employee_id):
        for emp in self.sales_people:
            if employee_id == emp.get_id():
                return emp
        return None

    def get_sale_frequencies(self):
        pass