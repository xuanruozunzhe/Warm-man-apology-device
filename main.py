import random
print("感谢您使用暖男道歉器，让我们开始吧！")
person=input("键入女友的昵称（输入‘@’显示随机昵称）：")
reason=input("键入道歉原因：")
if person=='@':
    nn=["宝宝","甜甜","小可爱","宝贝"]
    person=nn[random.randint(0,3)]
a=str(person+"真的对不起，都是我的错！")
b=str(person+"，我很愧疚，一直在反省自己的错误，我知道我因为"+reason+"惹"+person+"生气了，")
c=str(person+"我爱你，我发誓我再也不会让你生气了，我要用我的行动来证明，以后"+reason+"这种错误以后绝不会再犯！")
d=str("我真的深刻反省了很久，我真的不应该"+reason+"，")
e=str("如果"+person+"真的生气了，希望"+person+"可以原谅我，直到"+person+"原谅我，我才会原谅自己，")
f=str(person+"，我答应在你不高兴的时候哄你开心，再也不因为"+reason+"让你生气，我真的知道错了！")
g=str(person+"我看不到你的信息，听不到你的声音，想带你吹吹风，吹掉那些不愉快，只留下我给你的开心！")
output1=[a,b,c,d,e,f,g]
random.shuffle(output1)
print(*output1)
x=str("昨晚的夜空没有星星,就好像我的身边缺少了你，我真的不是故意让"+person+"生气的，回到我的身边来，好嘛？")
y=str("霓虹在夜晚将天空撕裂，悔恨的泪水在我眼前模糊，"+person+"，我想你了，原谅我好嘛？")
z=str("天空能放下冰雨，大海将包容游鱼，小草依赖着大地，原谅我无知的过去，我真诚地对你说对不起，"+person+"，不要离开我我好嘛？")
output2=[x,y]
random.shuffle(output2)
print(*output2,end="")
output3=str("想起我们曾经的甜蜜无间，让所有的不开心都烟消云散吧！"+person+"，我爱你！")
print(output3)
input()