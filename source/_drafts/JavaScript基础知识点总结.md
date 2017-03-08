---
title: JavaScript基础知识点总结
tags:
---

## 面向对象

### 创建对象的几种方法 

1.**工厂模式**

描述：使用函数创建属性和方法相同的对象。

缺点：没有解决对象识别的问题。

2.**构造函数模式**

描述： 特正是属性赋值给this, 需要使用 new 操作符，需要大写首字母。解决了对象识别问题，使用 constructor 和 instanceof 都能验证是否属于同一对象。

缺点：没有共享方法，浪费空间。

3.**原型模式**

描述：首先需要对原型对象的理解（实例，构造函数，原型对象三者指向关系）。把属性和方法都设置在构造函数的原型对象上面，解决了共享方法的问题。

缺点： 实例之间共享方法的同时也共享了引用类型的属性值。

4.**组合使用构造函数模式和原型模式**

描述：构造函数模式用于定义实例属性，原型模式用于定义方法和共享属性。

5.**动态原型模式**

描述：在构造函数内部使用条件判断需要的方法是否存在，否则在原型上定义需要的方法。

6.**寄生构造函数模式**
描述：跟工厂模式一样，多了使用 new 操作符。

6.**稳妥构造函数模式**

描述：跟寄生构造函数一样，不过在方法中不使用 this,同时不使用 new 操作符。

### 实现继承的几种方法

ECMAScript 函数没有签名，只支持实现继承，不支持接口继承。主要依靠原型链来实现。

1.**原型链**

描述：将子类型的构造函数的 prototype 指针指向父类型的一个实例。

缺点：父类型的实例中可能有引用类型的属性值，又会导致共享属性的问题。

2.**借用构造函数（伪造对象、经典继承）**

描述：在子类型的构造函数内部使用 call,apply 调用父类型的构造函数。可以传递参数。

缺点：父类型的方法都在子类型的构造函数中定义（而不是原型对象上），无法共享方法了。而且父类型原型中的方法也无法继承。

3.**组合继承（伪经典继承）**

描述：需要父类型在构造函数中定义非共享属性，在原型对象中定义方法。然后子类型在构造函数中用 call,apply 调用父类型的构造函数，然后把 prototype 指向父类型的一个实例。该模式是最常用的继承模式。

4.**原型式继承**

描述：借助原型可以基于已有对象创建新对象（借助空的构造函数）。本质上是对已有对象的浅复制。等于 Object.create()方法。

5.**寄生式继承**

描述：在原型式继承的基础上，内部做一些添加方法之类的行为，然后返回浅复制的对象。

6.**寄生组合式继承**

描述：组合继承中，会在指定子类型的 prototype 时生成一遍父类型的属性，又在子类型构造函数中借用父类型的构造函数生成了父类型的属性（同时屏蔽了 prototype 中的属性值，避免共享）。这样会浪费空间。寄生组合式继承在指定子类型的 prototype 时，通过原型式继承中的方法（浅复制+原型链关系）创建父类型原型的副本并赋值给子类型的 prototype 指针。从而避免在子类型原型中创建属性值。同时保持了原型链不变。

## 闭包

含义：闭包是指有权访问另一个函数作用域中的变量的函数。创建闭包的常用方式就是在函数内部创建另外一个函数。

### 作用域链

含义：当函数第一次被调用时，会创建一个执行上下文（execution context）和相应的作用域链，**作用域链的本质是指向一系列变量对象的指针列表**，它只引用但不实际包含变量对象。作用域链保存在函数的[[Scope]] 内部属性中，列表中的顺序依次是当前执行环境的变量对象，外一层包含函数的变量对象，外两层包含函数的变量对象，...，直至最外层全局对象（浏览器中是 window）。**变量对象**也是在函数执行时创建的一个对象，它包含有在函数内部创建的所有变量、函数参数和 this（指向活动对象的指针）,arguments（由函数参数组成的类数组对象） 等默认产生的属性。

### this 指针

含义：需要知道 **object.func() 中，func 中的 this 指向 object**，也即，函数执行时其所在的外层对象。而且可以通过`apply,call,bind`这三个方法来修改 this 的指向。

例子：
```
var name = "the window";
var object = {
    name:"object",
    getName:function(){
        return this.name;
    }
}
object.getName() //"object"
(object.getName)() //"object"
(object.getName=object.getName)() //"the window"
```
### 闭包的用处

1.模仿块级作用域 

2.构造私有变量（静态私有变量、模块模式）

### 闭包的缺点

1.可能会造成内存泄露
```
//下面例子中，unused 与 someMethod 都是 replaceThing 内部定义的闭包，因而在其作用域链中均存在对 replaceThing 的变量对象的引用，而由于 unused 使用了 originalThing 因而 unused 这个闭包所指向的 replaceThing 的变量对象中必须有 originalThing，同时由于变量对象引用一致性，相当于在 someMethod 中引用了 originalThing ，也即 theThing 会形成一个引用链表，导致内存泄露。

var theThing = null;
var replaceThing = function () {
  var originalThing = theThing;
  // Define a closure that references originalThing but doesn't ever
  // actually get called. But because this closure exists,
  // originalThing will be in the lexical environment for all
  // closures defined in replaceThing, instead of being optimized
  // out of it. If you remove this function, there is no leak.
  var unused = function () {
    if (originalThing)
      console.log("hi");
  };
  theThing = {
    longStr: new Array(1000000).join('*'),
    // While originalThing is theoretically accessible by this
    // function, it obviously doesn't use it. But because
    // originalThing is part of the lexical environment, someMethod
    // will hold a reference to originalThing, and so even though we
    // are replacing theThing with something that has no effective
    // way to reference the old value of theThing, the old value
    // will never get cleaned up!
    someMethod: function () {}
  };
  // If you add `originalThing = null` here, there is no leak.
};
setInterval(replaceThing, 1000);
```
