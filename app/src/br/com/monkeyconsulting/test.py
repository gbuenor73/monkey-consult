import justpy as jp


# wp = jp.WebPage()
# p = jp.P(text="teste", a=wp)


def hello_world():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp


def hello_world2():
    wp = jp.WebPage()
    for i in range(1, 11):
        jp.P(text=f"{i} Hello World", a=wp, style=f"font-size: {10 * i}px")
    return wp


def hello_world3():
    wp = jp.WebPage()
    my_paragraph_design = "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    for i in range(1, 11):
        jp.P(text=f"{i}) Hello World!", a=wp, classes=my_paragraph_design)
    return wp


wp = jp.WebPage(delete_flag=False)
my_paragraph_design = "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
for i in range(1, 11):
    jp.P(text=f"{i}) Hello World!", a=wp, classes=my_paragraph_design)


def hello_world4():
    return wp


def my_click1(self, msg):
    self.text = 'I was clicked'


def event_demo1():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', my_click1)
    return wp


def my_click2(self, msg):
    self.text = 'I was clicked'
    print(msg.event_type)
    print(msg['event_type'])
    print(msg)


def event_demo2():
    wp = jp.WebPage()
    d = jp.P(text='Not clicked yet', a=wp, classes='text-xl m-2 p-2 bg-blue-500 text-white')
    d.on('click', my_click2)
    return wp


def my_click3(self, msg):
    print(msg)
    self.text = 'I was clicked'


def event_demo3():
    wp = jp.WebPage()
    wp.debug = True
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', my_click3)
    d.additional_properties = ['screenX', 'pageY', 'altKey', 'which', 'movementX', 'button', 'buttons']
    return wp


def my_click4(self, msg):
    self.text = 'I was clicked'
    self.set_class('bg-blue-500')


def my_mouseenter(self, msg):
    self.text = 'Mouse entered'
    self.set_class('bg-red-500')


def my_mouseleave(self, msg):
    self.text = 'Mouse left'
    self.set_class('bg-green-500')


def event_demo4():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-64 text-2xl m-2 p-2 bg-blue-500 text-white',
               click=my_click4, mouseenter=my_mouseenter, mouseleave=my_mouseleave)
    return wp


def button_click1(self, msg):
    self.num_clicked += 1
    self.message.text = f'{self.text} clicked. Number of clicks: {self.num_clicked}'
    self.set_class('bg-red-500')
    self.set_class('bg-red-700', 'hover')


def event_demo5():
    number_of_buttons = 25
    wp = jp.WebPage()
    button_div = jp.Div(classes='flex m-4 flex-wrap', a=wp)
    button_classes = 'w-32 mr-2 mb-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'
    message = jp.Div(text='No button clicked yet', classes='text-2xl border m-4 p-2', a=wp)
    for i in range(1, number_of_buttons + 1):
        b = jp.Button(text=f'Button {i}', a=button_div, classes=button_classes, click=button_click1)
        b.message = message
        b.num_clicked = 0
    return wp


jp.justpy(event_demo5)
