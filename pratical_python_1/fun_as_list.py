sample_list = []
another_list = []
add_any_types_in_list = []

print(type(sample_list))

# the method dir show all method the class has
print(dir(sample_list))


def add_even_number_into_list():
    for i in range(20):
        if i % 2 == 0:
            sample_list.append(i)


def another_way_to_even_number():
    return [_ for _ in range(20) if _ % 2 == 0]


def show_values_in_list(a_list):
    print('Show values in list')
    for i, v in enumerate(a_list):
        print(f'\tlist[{i}] = {v} ')


add_even_number_into_list()
show_values_in_list(sample_list)

another_list = another_way_to_even_number()
show_values_in_list(another_list)

add_any_types_in_list.extend(another_list)
add_any_types_in_list.append('a text or string')
add_any_types_in_list.append(5.3)


class SampleAnClass:
    pass


a_object = SampleAnClass()

add_any_types_in_list.append(a_object)
show_values_in_list(add_any_types_in_list)

bi_dimession_list = [[1, 2], [3, 4]]
c_list = bi_dimession_list[:]

# id is a method same is hash of object
print('note that the elements is the same, but we have two object')
print(id(bi_dimession_list))
print(id(c_list))

show_values_in_list(bi_dimession_list)
show_values_in_list(c_list)

c_list[0].append(3)

show_values_in_list(c_list)
show_values_in_list(bi_dimession_list)



