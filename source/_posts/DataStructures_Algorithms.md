---
date: 2024-09-30 10:48:37
title: 数据结构和算法
tags: 
- 数据结构
- 算法
- C++
categories: 
- 数据结构
- 算法
---
# 数据结构和算法概述
```
数据结构就是指一组数据的存储结构。算法就是操作数据的一组方法。

数据结构和算法是相辅相成的。数据结构是为算法服务的，算法作用在特定的数据结构之上。 因此，我们无法孤立数据结构来讲算法，也无法孤立算法来讲数据结构。

数据结构是静态的，它只是组织数据的一种方式。如果不在它的基础上操作、构建算法，孤立存在的数据结构就是没用的。
```

# 数据结构

## 1、什么是数据结构？
- 数据结构是数据的组织、管理和存储格式，其使用目的是为了高效的访问和修改数据。
- 数据结构是算法的基石。如果把算法比喻成美丽灵动的舞者，那么数据结构就是舞者脚下广阔而坚实的舞台。

## 2、物理结构和逻辑结构的区别？
- 物理结构就像人的血肉和骨骼，看得见，摸得着，实实在在，如数组、链表。
- 逻辑结构就像人的思想和精神，它们看不见、摸不着，如队列、栈、树、图。

## 3、线性存储结构和非线性存储结构的区别？
- 线性：元素之间的关系是一对一的，如栈、队列。
- 非线性：每个元素可能连接0或多个元素，如树、图。

# 算法

## 1、什么是算法？
- 数学：算法是用于解决某一类问题的公式和思想。
- 计算机：一系列程序指令，用于解决特定的运算和逻辑问题。
## 2、如何衡量算法好坏？
- 时间复杂度：运行时间长短。
- 空间复杂度：占用内存大小。
## 3、怎么计算时间复杂度？
大O表示法（渐进时间复杂度）：把程序的相对执行时间函数T(n)简化为一个数量级，这个数量级可以是n、n^2、logN等。
### 推导时间复杂度的几个原则：
- 如果运行时间是常数量级，则用常数1表示。
- 只保留时间函数中的最高阶项。
- 如果最高阶项存在，则省去最高项前面的系数。
  
`时间复杂度对比：O(1) > O(logn) > O(n) > O(nlogn) > O(n^2)。`

## 4、怎么计算空间复杂度？
```
常量空间 O(1)：存储空间大小固定，和输入规模没有直接的关系。
线性空间 O(n)：分配的空间是一个线性的集合，并且集合大小和输入规模n成正比。
二维空间 O(n^2)：分配的空间是一个二维数组集合，并且集合的长度和宽度都与输入规模n成正比。
递归空间 O(logn)：递归是一个比较特殊的场景。虽然递归代码中并没有显式的声明变量或集合，但是计算机在执行程序时，会专门分配一块内存空间，用来存储“方法调用栈”。执行递归操作所需要的内存空间和递归的深度成正比。
```
## 5、如何定义算法稳定性？
- 稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
- 不稳定：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
## 6、有哪些常见算法？
首先要明确：特定算法解决特定问题。

- 字符串：暴力匹配、BM、KMP、Trie等。
- 查找：二分查找、遍历查找等。
- 排序：冒泡排序、快排、计数排序、堆排序等。
- 搜索：TFIDF、PageRank等。
- 聚类分析：期望最大化、k-meanings、k-数位等。
- 深度学习：深度卷积神经网络、生成式对抗等。
- 异常检测：k最近邻、局部异常因子等。
- ......
- 
其中，字符串、查找、排序算法是最基础的算法。

# 常见数据结构

## 线性表

## 数组
### 1）什么是数组？
    数据是有限个相同类型的变量所组成的有序集合。数组中的每一个变量被称为元素。

### 2）数组的基本操作？
    读取O(1)、更新O(1)、插入O(n)、删除O(n)、扩容O(n)。

## 链表

### 1）什么是链表？
    链表是一种在物理上非连续、非顺序的数据结构，由若干个节点组成。

    单向链表的每一个节点又包含两部分，一部分是存放数据的变量data，另一部分是指向下一个节点的指针next。

### 2）链表的基本操作？
    读取O(n)、更新O(1)、插入O(1)、删除O(1)。

### 3）链表 VS 数组
- 数组：适合多读、插入删除少的场景。
- 链表：适用于插入删除多、读少的场景。

## 栈

### 什么是栈？
    栈是一种线性逻辑数据结构，栈的元素只能后进先出。最早进入的元素存放的位置叫做栈底，最后进入的元素存放的位置叫栈顶。

    一个比喻，栈是一个一端封闭一端开放的中空管子，队列是两端开放的中空管子。

## 队列

### 什么是队列？
一种线性逻辑数据结构，队列的元素只能后进后出。队列的出口端叫做队头，队列的入口端叫做队尾。

### 队列的应用
```
消息队列
多线程的等待队列
网络爬虫的待爬URL队列
```

## 散列表（Hash Table）

- 散列表（哈希表）用的是数组支持按照下标随机访问数据的特性，所以散列（哈希）表其实就是数组的一种扩展，由数组演化而来。可以说，如果没有数组，就没有散列（哈希）表。

- 一种逻辑数据结构，提供了键（key）和值（value）的映射关系。

### 散列函数（哈希函数）
散列表两个核心问题是`散列函数设计和散列冲突解决`。

`散列（哈希）函数设计的基本要求：`
```
1.散列（哈希）函数计算得到的散列值是一个非负整数；

2.如果 key1 = key2，那 hash(key1) == hash(key2)；

3.如果 key1 ≠ key2，那 hash(key1) ≠ hash(key2)。

```

第一二点没啥问题，但第三点理解起来可能会有问题，要想找到一个不同的 key 对应的散列（哈希）值都不一样的散列（哈希）函数，几乎是不可能的。即便像业界著名的MD5、SHA、CRC等哈希算法，也无法完全避免这种散列冲突。而且，因为数组的存储空间有限，也会加大散列（哈希）冲突的概率。

### 什么是哈希(散列)冲突？
不同的key通过`哈希(散列)函数`获得的下标有可能是相同的，例如002936这个key对应的数组下标是2，002947对应的数组下标也是2，这种情况就是`哈希(散列)冲突`。

我们常用的散列（哈希）冲突解决方法有两种，`开放寻址法和链表法`。

`1. 开放寻址法`
开放寻址法的核心思想是，如果出现了散列（哈希）冲突，我们就重新探测一个空闲位置，将其插入。

`线性探测`：如果存储位置已经被占用了，我们就从当前位置开始，依次往后查找，看是否有空闲位置，直到找到为止。

`二次探测`：跟线性探测很像，线性探测每次探测的步长是 1，那它探测的下标序列就是 hash(key)+0，hash(key)+1，hash(key)+2……而二次探测探测的步长就变成了原来的“二次方”，也就是说，它探测的下标序列就是 hash(key)+0，hash(key)+12，hash(key)+22……

`双重散列`：意思就是不仅要使用一个散列（哈希）函数。我们使用一组散列（哈希）函数 hash1(key)，hash2(key)，hash3(key)……我们先用第一个散列（哈希）函数，如果计算得到的存储位置已经被占用，再用第二个散列（哈希）函数，依次类推，直到找到空闲的存储位置。

当数据量比较小、装载因子小的时候，适合采用`开放寻址法`。这也是 `Java` 中的`ThreadLocalMap`使用`开放寻址法`解决`散列（哈希）冲突`的原因。

`2. 链表法`
所有散列（哈希）值相同的元素我们都放到相同槽位对应的链表中。

`为什么HashMap使用链表法解决哈希冲突`
1、首先，链表法对内存的利用率比开放寻址法要高。因为链表结点可以在需要的时候再创建，并不需要像开放寻址法那样事先申请好。实际上，这方面链表优于数组。

2、链表法比起开放寻址法，`对大装载因子的容忍度更高`。开放寻址法只能适用装载因子小于 1 的情况。接近 1 时，就可能会有大量的散列（哈希）冲突，导致大量的探测、再散列（哈希）等，性能会下降很多。但是对于链表法来说，`只要散列（哈希）函数的值随机均匀，即便装载因子变成 10，也就是链表的长度变长了而已`，虽然查找效率有所下降，但是比起顺序查找还是快很多。

## 排序

### 插入排序

```

void insertion_sort(vector<int>& nums, int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = i; j > 0 && nums[j] < nums[j-1]; --j) {
            swap(nums[j], nums[j-1]);
        }
    }
}

// 引用
template <typename AnyType>

inline void Swap(AnyType &a, AnyType &b)
{
    AnyType temp;
    temp = a;
    a = b;
    b = temp;
}

// 指针
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

```

### 冒泡排序

```

void bubble_sort(vector<int>& nums, int n) {
    bool swapped;
    for (int i = 1; i < n; ++i) {
        swapped = false;
        for (int j = 1; j < n - i + 1; ++j) {
            if (nums[j] < nums[j-1]) {
                swap(nums[j], nums[j-1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
}

```

### 选择排序

```

void selection_sort(vector<int>& nums, int n) {
    int mid;
    for (int i = 0; i < n - 1; ++i) {
        mid = i;
        for (int j = i + 1; j < n; ++j) {
            if (nums[j] < nums[mid]) {
                mid = j;
            }
        }
        swap(nums[mid], nums[i]);
    }
}

```

### 快速排序

```
void sort() {
    vector<int> nums = {1,3,5,7,2,6,4,8,9,2,8,7,6,0,3,5,9,4,1,0};
    vector<int> temp(nums.size());
//    sort(nums.begin(), nums.end());
//    quick_sort(nums, 0, nums.size());
//    merge_sort(nums, 0, nums.size(), temp);
    insertion_sort(nums, nums.size());
    bubble_sort(nums, nums.size());
    selection_sort(nums, nums.size());
}

// 快速选择
int quickSelection(vector<int>& nums, int l, int r) {
    int i = l + 1, j = r;
    while (true) {
        while (i < r && nums[i] <= nums[l]) {
            ++i;
        }
        while (l < j && nums[j] >= nums[l]) {
            --j;
        }
        if (i >= j) {
            break;
        }
        swap(nums[i], nums[j]);
    }
    swap(nums[l], nums[j]);
    return j;
}

int findKthLargetst(vector<int>& nums, int k) {
    int l = 0, r = nums.size() - 1, target = nums.size() - k;
    while (l < r) {
        int mid = quickSelection(nums, l, r);
        if (mid == target) {
            return nums[mid];
        }
        if (mid < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return nums[l];
}

```

### 快排

```

// 快排
void quick_sort(vector<int>& nums, int l, int r) {
    if (l + 1 >= r) {
        return;
    }
    int first = 1, last = r - 1, key = nums[first];
    while (first < last) {
        while (first < last && nums[last] >= key) {
            --last;
        }
        nums[first] = nums[last];
        while (first < last && nums[first] <= key) {
            ++first;
        }
        nums[last] = nums[first];
    }
    nums[first] = key;
    quick_sort(nums, l, first);
    quick_sort(nums, first + 1, r);
}

void merge_sort(vector<int>& nums, int l, int r, vector<int>& temp) {
    if (l + 1 >= r) {
        return;
    }
    // divide
    int m = l + (r - 1) / 2;
    merge_sort(nums, l, m, temp);
    merge_sort(nums, m, r, temp);
    // conquer
    int p = l, q = m, i = l;
    while (p < m || q < r) {
        if (q >= r || (p < m && nums[p] <= nums[q])) {
            temp[i++] = nums[p++];
        } else {
            temp[i++] = nums[q++];
        }
    }
    for (i = l; i < r; ++i) {
        nums[i] = temp[i];
    }
}

```

### 桶排序

```

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> counts;
    int max_count = 0;
    for (const int & num : nums) {
        max_count = max(max_count, ++counts[num]);
    }
    
    vector<vector<int>> buckets(max_count + 1);
    for (const auto & p : counts) {
        buckets[p.second].push_back(p.first);
    }
    
    vector<int> ans;
    for (int i = max_count; i >= 0 && ans.size() < k; --i) {
        for (const int & num : buckets[i]) {
            ans.push_back(num);
            if (ans.size() == k) {
                break;
            }
        }
    }
    return ans;
}

```

### 归并 

### 希尔

### 基数排序

### 堆排序

### 二分查找 

## 树

### 什么是树？

树（tree）是n（n≥0）个节点的有限集。
当n=0时，称为空树。在任意一个非空树中，有如下特点：
- 有且仅有一个特定的称为根的节点。
- 当n>1时，其余节点可分为m（m>0）个互不相交的有限集，每一个集合本身又是一个树，并称为根的子树。

### 树的遍历？
1）深度优先
```
前序：根节点、左子树、右子树。
中序：左子树、根节点、右子树。
后序：左子树、右子树、根节点。
```
实现方式：递归或栈。

2）广度优先
```
层序：一层一层遍历。
```
实现方式：队列。

## 二叉树
```
1）什么是二叉树?
二叉树（binary tree）是树的一种特殊形式。二叉，顾名思义，这种树的每个节点最多有2个孩子节点。注意，这里是最多有2个，也可能只有1个，或者没有孩子节点。
2）什么是满二叉树?
一个二叉树的所有非叶子节点都存在左右孩子，并且所有叶子节点都在同一层级上，那么这个树就是满二叉树。
3）什么是完全二叉树?
对一个有n个节点的二叉树，按层级顺序编号，则所有节点的编号为从1到n。如果这个树所有节点和同样深度的满二叉树的编号为从1到n的节点位置相同，则这个二叉树为完全二叉树。
```

## B树 B+树 （多路查找树）

## 搜索二叉树 最大堆 最小堆 优先级队列

## 二叉查找树
### 1）什么是二叉查找树？
二叉查找树在二叉树的基础上增加了以下几个条件：
- 如果左子树不为空，则左子树上所有节点的值均小于根节点的值。
- 如果右子树不为空，则右子树上所有节点的值均大于根节点的值。
- 左、右子树也都是二叉查找树。

### 2）二叉查找树的作用？
- 查找==》二分查找。
- 排序==》中序遍历。
### 3）二叉树的实现方式？
- 链表。
- 数组：对于稀疏二叉树来说，数组表示法是非常浪费空间的。

## 二叉堆
### 什么是二叉堆？
二叉堆是一种特殊的完全二叉树，它分为两个类型：`最大堆`和`最小堆`。
- `最大堆`的任何一个父节点的值，都大于或等于它左、右孩子节点的值。
- `最小堆`的任何一个父节点的值，都小于或等于它左、右孩子节点的值。

##  红黑树 

树型结构主要用于搜索，一直是科学领域的重要演算法，当中探讨了树可能遇到的问题：`树的成长可能偏向于一边`，也就是`不平衡`现象。

`二叉树`是常见且广泛使用的一种树，面临其可能`退化成链表`的潜藏缺点，在使用上难免让人担心其效率。此外，在一些应用上，可能不希望这样的不平衡的可能性发生。所以具有自动平衡左右数量分布效果的演算算法早在 `1962 年`被提出，称为 `AVL 树`。这种平衡成长的二叉搜索树被称为`自平衡二叉搜索树`。

接下来，介绍同为自平衡`二叉搜索树`的`红黑树`对平衡性的要求比 `AVL 树`还要宽松。`红黑树`是利用`节点颜色`来检查二叉树每条路径的高度是否差不多，因为发明者定下了以下规则：
```
1.树上的每个结点(node) 只能是 红色 或 黑色。

2.根节点(root) 一定是黑色。

3.叶子节点(leaf) 一定是 黑色 的 空值节点 (NULL)。

4.任一路径上不能有两个连续的红色。注意：黑色节点的子节点颜色没有限制。

5.从任何节点出发，其下至叶节点所有路径的黑色节点数目相同。
```

满足上述的二叉树，相比一般的二叉树更能保持平衡性，往后套用二叉树的算法来查找时能更快速、方便的到达目的地，套用算法的时间复杂度为 `O(logn)`，因为`红黑树保证最长路径不会超过最短路径的两倍`（由`规则 4 和规则 5`）。原因是：当某条路径最短时，这条路径必然都是由黑色节点构成。当某条路径长度最长时，这条路径必然是由红色和黑色节点相间构成（规则4限定了不能出现两个连续的红色节点）。而`规则5`又限定了从任一节点到其每个叶子节点的所有路径必须包含相同数量的黑色节点。此时，在路径最长的情况下，路径上红色节点数量 = 黑色节点数量。该路径长度为两倍黑色节点数量，也就是最短路径长度的 2 倍。

## Tire树 

* Trie 树，也叫“字典树”。顾名思义，它是一个树形结构。它是一种专门处理字符串匹配的数据结构，用来解决在一组字符串集合中快速查找某个字符串的问题。

```

class TrieNode {
public:
    TrieNode* childNode[26];
    bool isVal;
    TrieNode(): isVal(false) {
        for (int i = 0; i < 26; ++i) {
            childNode[i] = nullptr;
        }
    }
};

class Trie {
    TrieNode* root;
public:
    Trie(): root(new TrieNode()) {}
    
    // 向字典树插入一个词
    void insert(string word) {
        TrieNode* temp = root;
        for (int i = 0; i < word.size(); ++i) {
            if (!temp->childNode[word[i]-'a']) {
                temp->childNode[word[i]-'a'] = new TrieNode();
            }
            temp = temp->childNode[word[i]-'a'];
        }
        temp->isVal = true;
    }
    
    // 判断字典树里是否有一个词
    bool search(string word) {
        TrieNode* temp = root;
        for (int i = 0; i < word.size(); ++i) {
            if (!temp) {
                break;
            }
            temp = temp->childNode[word[i]-'a'];
        }
        return temp ? temp->isVal : false;
    }
    
    // 判断字典树是否有一个以词开始的前缀
    bool startWith(string prefix) {
        TrieNode* temp = root;
        for (int i = 0; i < prefix.size(); ++i) {
            if (!temp) {
                break;
            }
            temp = temp->childNode[prefix[i]-'a'];
        }
        return temp;
    }
};

```

## 广度遍历搜索树

```

template <class T>
class BST {
    struct Node {
        T data;
        Node* left;
        Node* right;
    };
    Node* root;
    
    Node* makeEmpty(Node* t) {
        if (t == NULL) return NULL;
        makeEmpty(t->left);
        makeEmpty(t->right);
        delete t;
        return NULL;
    }
    
    Node* insert(Node* t, T x) {
        if (t == NULL) {
            t = new Node;
            t->data = x;
            t->left = t->right = NULL;
        } else if (x < t->data) {
            t->left = insert(t->left, x);
        } else if (x > t->data) {
            t->right = insert(t->right, x);
        }
        return t;
    }
    
    Node* find(Node* t, T x) {
        if (t == NULL) {
            return NULL;
        }
        if (x < t->data) {
            return find(t->left, x);
        }
        if (x > t->data) {
            return find(t->right, x);
        }
        return t;
    }
    
    Node* findMin(Node* t) {
        if (t == NULL || t->left == NULL) {
            return t;
        }
        return findMin(t->left);
    }
    
    Node* findMax(Node* t) {
        if (t == NULL || t->right == NULL) {
            return t;
        }
        return findMax(t->right);
    }
    
    Node* remove(Node* t, T x) {
        Node* temp;
        if (t == NULL) {
            return NULL;
        } else if (x < t->data) {
            t->left = remove(t->left, x);
        } else if (x > t->data) {
            t->right = remove(t->right, x);
        } else if (t->left && t->right) {
            temp = findMin(t->right);
            t->data = temp->data;
            t->right = remove(t->right, t->data);
        } else {
            temp = t;
            if (t->left == NULL) {
                t = t->right;
            } else if (t->right == NULL) {
                t = t->left;
            }
            delete temp;
        }
        return t;
    }
public:
    BST(): root(NULL) {}
    
    ~BST() {
        root = makeEmpty(root);
    }
    
    void insert(T x) {
        insert(root, x);
    }
    
    void remove(T x) {
        remove(root, x);
    }
};

```

## 哈夫曼 LWZ算法 

### 赫夫曼树（Huffman Tree）：

1.给定 n 个 `权值` 作为 n 个 `叶子节点`，构造一颗二叉树，`若该树的 带权路径长度（WPL）达到最小`，称这样的二叉树为 `最优二叉树`，也称为 `哈夫曼树（Huffman Tree）`，还有的叫 `霍夫曼树`
2.赫夫曼树是带权路径长度最短的树，`权值较大的节点离根节点较近`
具体细节请看[百度百科--哈夫曼树](https://baike.baidu.com/item/%E5%93%88%E5%A4%AB%E6%9B%BC%E6%A0%91/2305769)

`路径`:从树中一个结点到另一个结点之间的分支构成这两个结点间的路径。

`结点的路径长度`:两结点间路径上的分支数。

`树的路径长度`：从树根到每一个结点的路径长度之和。

`权(weight)又称权重`：将树中结点赋给一个有着某种含义的数值，(具体的意义根据树使用的场合确定)则这个数值称为该结点的权。

`结点的带权路径长度`：从根结点到该结点之间的路径长度与结点上权的乘积。

`树的带权路径长度`:树中所有叶子结点的带权路径长度之和。

`树的路径长度`:从树根到每一个结点的路径长度之和。

`哈夫曼树`:最优树，带权路径长度(WPL)最短的树。

“`带权路径长度最短`”是在“度相同”的树中比较而得的结果,因此有最优二叉树、最优三叉树之称。

`哈夫曼树`:最优二叉树，带权路径长度(WPL)最短的二叉树，因为构造这种树的算法是由`哈夫曼教授`于`1952年`提出的,所以被称为`哈夫曼树`,相应的算法称为`哈夫曼算法`。

### 哈夫曼树的构造
假设有n个权值，则构造出的哈夫曼树有n个叶子结点。 n个权值分别设为 w1、w2、…、wn，则哈夫曼树的构造规则为：

```
(1) 将w1、w2、…，wn看成是有n 棵树的森林(每棵树仅有一个结点)；

(2) 在森林中选出两个根结点的权值最小的树合并，作为一棵新树的左、右子树，且新树的根结点权值为其左、右子树根结点权值之和；

(3)从森林中删除选取的两棵树，并将新树加入森林；

(4)重复(2)、(3)步，直到森林中只剩一棵树为止，该树即为所求得的哈夫曼树。
```

### 哈夫曼树的应用：哈夫曼编码

### 引言
`哈夫曼编码的介绍`

哈夫曼编码是一种压缩编码的编码算法，是基于哈夫曼树的一种编码方式。哈夫曼树又称为带权路径长度最短的二叉树。

哈夫曼编码跟 ASCII 编码有什么区别？ASCII 编码是对照ASCII 表进行的编码，每一个字符符号都有对应的编码，其编码长度是固定的。而哈夫曼编码对于不同字符的出现频率其使用的编码是不一样的。其会对频率较高的字符使用较短的编码，频率低的字符使用较高的编码。这样保证总体使用的编码长度会更少，从而实现到了数据压缩的目的。

举一个例子：对字符串“aaa bb cccc dd e”使用 ASCII 进行编码得到的结果为：97 97 97 32 98 98 32 99 99 99 99 32 100 100 32 101 （十进制）需要 16 个字节，如果使用二进制表示的话需要 128位的内存空间去存储。

而如果使用 Unicode 的话会更多，因为 Unicode 又称为万国码，内容更多，因此使用的空间也需要更大。

接下来使用哈夫曼编码对上面的字符串进行编码。看看需要多大的空间

### 统计频率
上面的介绍已经说明了哈夫曼编码会根据字符出现的频率从而条件字符使用的编码长度。因此要先求出这个字符串中每个字符出现的频率

字符 | c | ''空 | a | b | d | e 
:-:|:-:|:-:|:-:|:-:|:-:|:-:
频率 | 4 | 4 | 3 | 2 | 2 | 1 

### 构建哈夫曼树

`排序`
哈夫曼树是一个带权的二叉树，而在哈夫曼编码中，字符的出现频率就是字符的权重。因此要根据字符的频率放入优先队列中进行排序。然后根据这些字符构建一棵哈夫曼树

字符 | e | d | b | a | ''空 | c 
:-:|:-:|:-:|:-:|:-:|:-:|:-:
频率 | 1 | 2 | 2 | 3 | 4 | 4 

将队列中的每一个元素（字符）都看成一棵树。

`合并`

进行迭代，每次都去除队列中的前面两个元素，也就是权值最小的两棵子树进行合并成一棵子树。直到最终所有的元素合并成一棵树。这棵树就是哈夫曼树。

合并后生成的树，最终只有一棵树，该树便是这个字符串所生成的哈夫曼树.
### 为哈夫曼树进行编码
将二叉树分支中的左分支编为 0，右分支编为 1：
![哈夫曼树](<images/huffmanTree.jpg>)

可以发现每个字符都在树的叶子节点上，因此要获取每个字符的哈夫曼编码，就通过根节点遍历到对应的子节点所经历的路径就是这个字符的编码：

字符|e|d|b|a|''|c
:-:|:-:|:-:|:-:|:-:|:-:|:-:
编码|1110|1111|110|00|01|10

可以发现使用频率高的字符c 其编码长度是比出现频率低的字符e 编码长度要少。最后计算使用哈夫曼编码的字符串“aaa bb cccc dd e”要使用多少位的内存空间进行存储：出现次数 * 编码长度。结果为 2 * 3 + 2 * 3 + 4 * 2 + 2 * 4 + 4 * 1 + 4 * 2 = 40位，与 ASCII 对应的 128位，少了2/3的存储空间。

## LWZ基本概念
`LZW压缩编码`是一种先进的数据压缩技术，属于无损压缩编码，该编码主要用于图像数据的压缩。对于简单图像和平滑且噪声小的信号源具有较高的压缩比，并且有较高的压缩和解压缩速度。

`LZW算法`是通过建立一个字符串表，用较短的代码来表示较长的字符串来实现压缩。LZW算法的`核心`就是算法词典的建立，通过词典实现对重复字符串的压缩。


## 动态规划 

### 爬楼梯问题

```

int _climbStairs(int n) {
    if (n < 2) {
        return n;
    }
    vector<int> dp(n + 1, 1);
    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}

// 给定 n 节台阶，每次可以走一步或走两步，求一共有多少种方式可以走完这些台阶。
int climbStairs(int n) {
    if (n <= 2) {
        return n;
    }
    int pre2 = 1, pre1 = 2, cur = 0;
    for (int i = 2; i < n; ++i) {
        cur = pre1 + pre2;
        pre2 = pre1;
        pre1 = cur;
    }
    return cur;
}


```

### 最长递增子序列的长度 

```

// 输入是一个一维数组，输出是一个正整数，表示最长递增子序列的长度。
//   Input: [10,9,2,5,3,7,101,18]
//   Output: 4
// 在这个样例中，最长递增子序列之一是 [2,3,7,18]。

int _lengthOfLIS(vector<int>& nums) {
    int max_length = 0, n = nums.size();
    if (n <= 1) {
        return n;
    }
    vector<int> dp(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        max_length = max(max_length, dp[i]);
    }
    return max_length;
}

int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    if (n <= 1) {
        return n;
    }
    vector<int> dp;
    dp.push_back(nums[0]);
    for (int i = 1; i < n; ++i) {
        if (dp.back() < nums[i]) {
            dp.push_back(nums[i]);
        } else {
            auto itr = lower_bound(dp.begin(), dp.end(), nums[i]);
            *itr = nums[i];
        }
    }
    return dp.size();
}

```


### 最长公共子序列

```

//输入是两个字符串，输出是一个整数，表示它们满足题目条件的长度。
//Input: text1 = "abcde", text2 = "ace"
//Output: 3
//在这个样例中，最长公共子序列是“ace”。
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length(), n = text2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (text1[i-1] == text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}

```

### 背包问题

```

//我们可以用动态规划来解决背包问题。以 0-1 背包问题为例。我们可以定义一个二维数组 dp 存储最大价值，
其中 dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到的最大价值。在我们遍 历到第 i 件物品时，
在当前背包总容量为 j 的情况下，如果我们不将物品 i 放入背包，那么 dp[i][j] = dp[i-1][j]，即前 i 个
物品的最大价值等于只取前 i-1 个物品时的最大价值;如果我们将物品 i 放 入背包，假设第 i 件物品体积为 w，
价值为 v，那么我们得到 dp[i][j] = dp[i-1][j-w] + v。我们只需 在遍历过程中对这两种情况取最大值即
可，总时间复杂度和空间复杂度都为 O(NW)。

int _knapsack(vector<int> weights, vector<int> values, int N, int W) {
    vector<vector<int>> dp(N + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= N; ++i) {
        int w = weights[i-1], v = values[i-1];
        for (int j = 1; j <= W; ++j) {
            if (j >= w) {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v);
            } else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    return dp[N][W];
}

int knapsack(vector<int> weights, vector<int> values, int N, int W) {
    vector<int> dp(W + 1, 0);
    for (int i = 1; i <= N; ++i) {
        int w = weights[i-1], v = values[i-1];
        for (int j = W; j >= w; --j) {
            dp[j] = max(dp[j], dp[j-w] + v);
        }
    }
    return dp[W];
}

int knapsack_(vector<int> weights, vector<int> values, int N, int W) {
    vector<int> dp(W + 1, 0);
    for (int i = 1; i <= N; ++i) {
       int w = weights[i-1], v = values[i-1];
       for (int j = w; j <= W; ++j) {
          dp[j] = max(dp[j], dp[j-w] + v);
       }
    }
    return dp[W];
}


```

### 字符串分割

```

//Input: s = "applepenapple", wordDict = ["apple", "pen"]
//Output: true
//在这个样例中，字符串可以被分割为 [“apple”,“pen”,“apple”]。
bool wordBreak(string s, vector<string>& wordDict) {
    int n = s.length();
    if (n <= 0) {
        return false;
    }
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; ++i) {
        for (const string & word: wordDict) {
            int len = word.length();
            if (i >= len && s.substr(i - len, len) == word) {
                dp[i] = dp[i] || dp[i - len];
            }
        }
    }
    return dp[n];
}

```

### 反转链表

```

ListNode* ReverseListNew(ListNode* pHead) {
    ListNode *pNode = pHead;
    ListNode *pPrev = NULL;
    while (pNode != NULL) {
        ListNode *pNext = pNode->m_pNext;
        pNode->m_pNext = pPrev;
        
        pPrev = pNode;
        pNode = pNext;
    }
    return pPrev;
}

ListNode *reverseList_DiguiNew(ListNode* pHead, ListNode* pHead2 = NULL) {
    if (pHead == NULL) {
        return pHead2;
    }
    ListNode *pNext = pHead->m_pNext;
    pHead->m_pNext = pHead2;
    return reverseList_DiguiNew(pNext, pHead);
}

```

### 合并两个链表

```

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (!l2) {
        return l1;
    }
    if (!l1) {
        return l2;
    }
    if (l1->m_nValue > l2->m_nValue) {
        l2->m_pNext = mergeTwoLists(l1, l2->m_pNext);
        return l2;
    }
    l1->m_pNext = mergeTwoLists(l1->m_pNext, l2);
    return l1;
}

ListNode* mergeTwoListsNew(ListNode *l1, ListNode *l2) {
    ListNode *dummy = new ListNode(), *node = dummy;
    while (l1 && l2) {
        if (l1->m_nValue <= l2->m_nValue) {
            node->m_pNext = l1;
            l1 = l1->m_pNext;
        } else {
            node->m_pNext = l2;
            l2 = l2->m_pNext;
        }
        node = node->m_pNext;
    }
    node->m_pNext = l1? l1 : l2;
    return dummy->m_pNext;
}

```

### 最优路径

```

//题目描述
//给定一个 m × n 大小的非负整数矩阵，求从左上角开始到右下角结束的、经过的数字的和最 小的路径。每次只能向右或者向下移动。
//输入输出样例
//  输入是一个二维数组，输出是最优路径的数字和。
//Input:
//[[1,3,1],
//[1,5,1],
// [4,2,1]]
//Output: 7
//在这个样例中，最短路径为 1->3->1->1->1。 题解
//我们可以定义一个同样是二维的 dp 数组，其中 dp[i][j] 表示从左上角开始到 (i, j) 位置的最 优路径的数字和。因为每次只能向下或者向右移动，我们可以很容易得到状态转移方程 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]，其中 grid 表示原数组。

int _minPathSum(vector<vector<int>>& grid) {
    size_t m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) {
                dp[i][j] = grid[i][j];
            } else if (i == 0) {
                dp[i][j] = dp[i][j-1] + grid[i][j];
            } else if (j == 0) {
                dp[i][j] = dp[i-1][j] + grid[i][j];
            } else {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
    }
    return dp[m-1][n-1];
}

int minPathSum(vector<vector<int>>& grid) {
    size_t m = grid.size(), n = grid[0].size();
    vector<int> dp(n, 0);
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) {
                dp[j] = grid[i][j];
            } else if (i == 0) {
                dp[j] = dp[j - 1] + grid[i][j];
            } else if (j == 0) {
                dp[j] = dp[j] + grid[i][j];
            } else {
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j];
            }
        }
    }
    return dp[n-1];
}

int minDistance(string word1, string word2) {
    int m = word1.length(), n = word2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i <= m; ++i) {
        for (int j = 0; j <= n; ++j) {
            if (i == 0) {
                dp[i][j] = j;
            } else if (j == 0) {
                dp[i][j] = i;
            } else {
                dp[i][j] = min(dp[i-1][j-1] + ((word1[i-1] == word2[j-1]) ? 0 : 1), min(dp[i-1][j] + 1, dp[i][j-1] + 1));
            }
        }
    }
    return dp[m][n];
}


```

```

//输入是一个一维数组，表示每个房子的钱财数量;输出是劫匪可以最多抢劫的钱财数量。
//Input: [2,7,9,3,1]
//Output: 12

//定义一个数组 dp，dp[i] 表示抢劫到第 i 个房子时，可以抢劫的最大数量。我们考虑 dp[i]， 此时可以抢劫的最大数量有两种可能，一种是我们选择不抢劫这个房子，此时累计的金额即为 dp[i-1];另一种是我们选择抢劫这个房子，那么此前累计的最大金额只能是 dp[i-2]，因为我们不 能够抢劫第 i-1 个房子，否则会触发警报机关。因此本题的状态转移方程为 dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])。

int _rob(vector<int> & nums) {
    if (nums.empty()) {
        return 0;
    }
    size_t n = nums.size();
    vector<int> dp(n + 1, 0);
    dp[1] = nums[0];
    for (int i = 2; i <= n; ++i) {
        dp[i] = max(dp[i-1], nums[i-1] + dp[i-2]);
    }
    return dp[n];
}
   
int rob(vector<int> & nums) {
    if (nums.empty()) {
        return 0;
    }
    size_t n = nums.size();
    if (n == 1) {
        return nums[0];
    }
    int pre2 = 0, pre1 = 0, cur = 0;
    for (int i = 0; i < n; ++i) {
        cur = max(pre2 + nums[i], pre1);
        pre2 = pre1;
        pre1 = cur;
    }
    return cur;
}

//int numberOfAritheticSlices(vector<int>& nums) {
//    int n = nums.size();
//    if (n < 3) {
//        return 0;
//    }
//    vector<int> dp(n, 0);
//    for (int i = 2; i < n; ++i) {
//        if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
//            dp[i] = dp[i-1] + 1;
//        }
//    }
//    return accumlate(dp.begin(), dp.end(), 0);
//}



vector<vector<int>> updateMartix(vector<vector<int>>& matrix) {
    if (matrix.empty()) {
        return {};
    }
    int n = matrix.size(), m = matrix[0].size();
    vector<vector<int>> dp(n, vector<int>(m, INT_MAX - 1));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; ++j) {
            if (matrix[i][j] == 0) {
                dp[i][j] = 0;
            } else {
                if (j > 0) {
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1);
                }
                if (i > 0) {
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1);
                }
            }
        }
    }
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            if (matrix[i][j] != 0) {
                if (j < m - 1) {
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1);
                }
                if (i < n - 1) {
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1);
                }
            }
        }
    }
    return dp;
}

int maximalSquare(vector<vector<char>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) {
        return 0;
    }
    int m = matrix.size(), n = matrix[0].size(), max_side = 0;
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (matrix[i-1][j-1] == '1') {
                dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1;
            }
            max_side = max(max_side, dp[i][j]);
        }
    }
    return max_side * max_side;
}

//题目描述
//  给定一个正整数，求其最少可以由几个完全平方数相加构成。
//输入输出样例
//– 47/143 –
//  输入是给定的正整数，输出也是一个正整数，表示输入的数字最少可以由几个完全平方数相 加构成。
//Input: n = 13
//Output: 2
//在这个样例中，13 的最少构成方法为 4+9。 题解
//对于分割类型题，动态规划的状态转移方程通常并不依赖相邻的位置，而是依赖于满足分割 条件的位置。我们定义一个一维矩阵 dp，其中 dp[i] 表示数字 i 最少可以由几个完全平方数相加 构成。在本题中，位置 i 只依赖 i - k2 的位置，如 i - 1、i - 4、i - 9 等等，才能满足完全平方分割 的条件。因此 dp[i] 可以取的最小值即为 1 + min(dp[i-1], dp[i-4], dp[i-9] · · · )。

int numSquares(int n) {
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j * j <= i; ++j) {
            dp[i] = min(dp[i], dp[i-j*j] + 1);
        }
    }
    return dp[n];
}

int numDecodings(string s) {//"226"  BZ(2 26)、VF(22 6) 或 BBF(2 2 6)
    int n = s.length();
    if (n == 0) {
        return 0;
    }
    int prev = s[0] - '0';
    if (!prev) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    vector<int> dp(n + 1, 1);
    for (int i = 2; i <= n; ++i) {
        int cur = s[i-1] - '0';
        if ((prev == 0 || prev > 2) && cur == 0) {
            return 0;
        }
        if ((prev < 2 && prev > 0) || (prev == 2 && cur < 7)) {
            if (cur) {
                dp[i] = dp[i-2] + dp[i-1];
            } else {
                dp[i] = dp[i-2];
            }
        } else {
            dp[i] = dp[i-1];
        }
        prev = cur;
    }
    return dp[n];
}





// 输入是一个一维正整数数组，输出时一个布尔值，表示是否可以满足题目要求。
//Input: [1,5,11,5]
//Output: true
//在这个样例中，满足条件的分割方法是 [1,5,5] 和 [11]。
bool _canPartition(vector<int> &nums) {
//    int sum = accumulate(nums.begin(), nums.end(), 0);
    int sum = 0;
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++) {
        sum += *it;
    }
    if (sum % 2) {
        return false;
    }
    int target = sum / 2, n = nums.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));
    for (int i = 0; i <= n; ++i) {
        dp[i][0] = true;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = nums[i-1]; j <= target; ++j) {
            dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i-1]];
        }
    }
    return dp[n][target];
}

bool canPartition(vector<int> &nums) {
//    int sum = accumulate(nums.begin(), nums.end(), 0);
    int sum = 0;
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++) {
        sum += *it;
    }
    if (sum % 2) {
        return false;
    }
    int target = sum / 2, n = nums.size();
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; ++i) {
        for (int j = target; j >= nums[i-1]; --j) {
            dp[j] = dp[j] || dp[j-nums[i-1]];
        }
    }
    return dp[target];
}

// 辅函数
pair<int, int> count(const string & s) {
    int count0 = s.length(), count1 = 0;
    for (const char & c: s) {
        if (c == '1') {
            ++count1;
            --count0;
        }
    }
    return make_pair(count0, count1);
}

// 主函数
int findMaxForm(vector<string>& strs, int m, int n) {
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (const string & str: strs) {
        auto [count0, count1] = count(str);
        for (int i = m; i >= count0; --i) {
            for (int j = n; j >= count1; --j) {
                dp[i][j] = max(dp[i][j], 1 + dp[i-count0][j-count1]);
            }
        }
    }
    return dp[m][n];
}

int coinChange(vector<int>& coins, int amount) {
    if (coins.empty()) {
        return -1;
    }
    vector<int> dp(amount + 1, amount + 2);
    dp[0] = 0;
    for (int i = 1; i <= amount; ++i) {
        for (const int & coin: coins) {
            if (i >= coin) {
                dp[i] = min(dp[i], dp[i-coin] + 1);
            }
        }
    }
    return dp[amount] == amount + 2 ? - 1 : dp[amount];
}



//输入一个一维整数数组，表示每天的股票价格;输出一个整数，表示最大的收益。
//
//7.8 股票交易 – 60/143 – Input: [7,1,5,3,6,4]
//Output: 5
//在这个样例中，最大的利润为在第二天价格为 1 时买入，在第五天价格为 6 时卖出。
int maxProfit(vector<int>& prices) {
    int sell = 0, buy = INT_MIN;
    for (int i = 0; i < prices.size(); ++i) {
        buy = max(buy, -prices[i]);
        sell = max(sell, buy + prices[i]);
    }
    return sell;
}

//输入一个一维整数数组，表示每天的股票价格;以及一个整数，表示可以买卖的次数 k。输 出一个整数，表示最大的收益。
//Input: [3,2,6,5,0,3], k = 2
//Output: 7
//在这个样例中，最大的利润为在第二天价格为 2 时买入，在第三天价格为 6 时卖出;再在第 五天价格为 0 时买入，在第六天价格为 3 时卖出。
int maxProfitUnlimited(vector<int> prices) {
    int maxProfit = 0;
    for (int i = 1; i < prices.size(); ++i) {
        if (prices[i] > prices[i-1]) {
            maxProfit += prices[i] - prices[i-1];
        }
    }
    return maxProfit;
}

int maxiumProfit(int k, vector<int>& prices) {
    int days = prices.size();
    if (days < 2) {
        return 0;
    }
    if (k >= days) {
        return maxProfitUnlimited(prices);
    }
    vector<int> buy(k + 1, INT_MIN), sell(k + 1, 0);
    for (int i = 0; i < days; ++i) {
        for (int j = 1; j <= k; ++j) {
            buy[j] = max(buy[j], sell[j-1] - prices[i]);
            sell[j] = max(sell[j], buy[j] + prices[i]);
        }
    }
    return sell[k];
}


```

## 贪心算法 

## 回溯法

```

//给定一个整数 n 和一个整数 k，求在 1 到 n 中选取 k 个数字的所有组合方法。
//
//6.3 回溯法 输入输出样例
//输入是两个正整数 n 和 k，输出是一个二维数组，表示所有组合方式。 Input: n = 4, k = 2
//Output: [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
void backtracking(vector<vector<int>>& ans, vector<int>& comb, int& count, int pos, int n, int k) {
    if (count == k) {
        ans.push_back(comb);
        return;
    }
    for (int i = pos; i <= n; ++i) {
        comb[count++] = i; // 修改当前节点状态
        backtracking(ans, comb, count, i + 1, n, k); // 递归子节点
        --count; // 回改当前节点状态
    }
}

vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> ans;
    vector<int> comb(k, 0);
    int count = 0;
    backtracking(ans, comb, count, 1, n, k);
    return ans;
}

//输入是一个二维字符数组和一个字符串，输出是一个布尔值，表示字符串是否可以被寻找 到。
//Input: word = "ABCCED", board =
//[[’A’,’B’,’C’,’E’],
// [’S’,’F’,’C’,’S’],
// [’A’,’D’,’E’,’E’]]
//Output: true
//从左上角的’A’ 开始，我们可以先向右、再向下、最后向左，找到连续的"ABCCED"。
void backtracking(int i, int j, vector<vector<char>>& board, string& word, bool
                  & find, vector<vector<bool>>& visited, int pos) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size()) {
        return;
    }
    if (visited[i][j] || find || board[i][j] != word[pos]) {
        return;
    }
    if (pos == word.size() - 1) {
        find = true;
        return;
    }
    visited[i][j] = true; // 修改当前节点状态
    // 递归子节点
    backtracking(i + 1, j, board, word, find, visited, pos + 1);
    backtracking(i - 1, j, board, word, find, visited, pos + 1);
    backtracking(i, j + 1, board, word, find, visited, pos + 1);
    backtracking(i, j - 1, board, word, find, visited, pos + 1);
    visited[i][j] = false; // 回改当前节点状态
}

bool exist(vector<vector<char>>& board, string word) {
    if (board.empty()) return false;
    int m = board.size(), n = board[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    bool find = false;
    for (int i = 0; i < m; ++i) {
       for (int j = 0; j < n; ++j) {
           backtracking(i, j, board, word, find, visited, 0);
       }
    }
    return find;
}

// 输入是一个整数 n，输出是一个二维字符串数组，表示所有的棋盘表示方法。
//Input: 4
//Output: [
// [".Q..", // Solution 1
//  "...Q",
//  "Q...",
//  "..Q."],
// ["..Q.", // Solution 2
//  "Q...",
//  "...Q",
//  ".Q.."]
//]
//在这个样例中，点代表空白位置，Q 代表皇后。
void backtracking(vector<vector<string>>& ans, vector<string>& board, vector<bool>& column, vector<bool>& ldiag, vector<bool>& rdiag, int row, int n) {
    if (row == n) {
        ans.push_back(board);
        return;
    }
    for (int i = 0; i < n; ++i) {
        if (column[i] || ldiag[n-row+i-1] || rdiag[row+i+1]) {
            continue;
        }
        // 修改当前节点状态
        board[row][i] = 'Q';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i+1] = true;
        // 递归子节点
        backtracking(ans, board, column, ldiag, rdiag, row+1, n);
        // 回改当前节点状态
        board[row][i] = '.';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i+1] = false;
    }
}

// 主函数
vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> ans;
    if (n == 0) {
        return ans;
    }
    vector<string> board(n, string(n, '.'));
    vector<bool> column(n, false), ldiag(2*n-1, false), rdiag(2*n-1, false);
    backtracking(ans, board, column, ldiag, rdiag, 0, n);
    return ans;
}

bool isBipartitle(vector<vector<int>>& graph) {
    int n = graph.size();
    if (n == 0) {
        return true;
    }
    vector<int> color(n, 0);
    queue<int> q;
    for (int i = 0; i < n; ++i) {
        if (!color[i]) {
            q.push(i);
            color[i] = 1;
        }
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (const int & j: graph[node]) {
                if (color[j] == 0) {
                    q.push(j);
                    color[j] = color[node] == 2 ? 1 : 2;
                } else if (color[node] == color[j]) {
                    return false;
                }
            }
        }
    }
    return true;
}

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> graph(numCourses, vector<int>());
    vector<int> indegree(numCourses, 0), res;
    for (const auto & prerequisite: prerequisites) {
        graph[prerequisite[1]].push_back(prerequisite[0]);
        ++indegree[prerequisite[0]];
    }
    queue<int> q;
    for (int i = 0; i < indegree.size(); ++i) {
        if (!indegree[i]) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        int u = q.front();
        res.push_back(u);
        q.pop();
        for (auto v: graph[u]) {
            --indegree[v];
            if (!indegree[v]) {
                q.push(v);
            }
        }
    }
    for (int i = 0; i < indegree.size(); ++i) {
        if (indegree[i]) {
            return vector<int>();
        }
    }
    return res;
}


char FirstNotRepeatingChar(char *pString) {
    if (pString == NULL) {
        return '\0';
    }
    const int tableSize = 256;
    unsigned int hashTable[tableSize];
    for (unsigned int i = 0; i < tableSize; ++i) {
        hashTable[i] = 0;
    }
    
    char* pHashKey = pString;
    while (*pHashKey !='\0') {
        hashTable[*pHashKey]++;
        pHashKey++;
    }
    
    pHashKey = pString;
    while (*pHashKey !='\0') {
        if (hashTable[*pHashKey] == 1) {
            return *pHashKey;
        }
        pHashKey++;
    }
    return '\0';
}



int helper(TreeNode *root) {
    if (!root) {
        return 0;
    }
    int left = helper(root->left), right = helper(root->right);
    if (left == -1 || right == -1 || abs(left - right) > 1) {
        return -1;
    }
    return 1 + max(left, right);
}

bool isBalanced(TreeNode *root) {
    return helper(root) != -1;
}

int helper(TreeNode* node, int& diameter) {
    if (!node) {
        return 0;
    }
    int l = helper(node->left, diameter);
    int r = helper(node->right, diameter);
    diameter = max(l + r, diameter);
    return max(l, r) + 1;
}

int diameterOfBinaryTree(TreeNode* root) {
    int diameter = 0;
    helper(root, diameter);
    return diameter;
}

int pathSumStartWithRoot(TreeNode* root, int sum) {
    if (!root) {
        return 0;
    }
    int count = root->val == sum ? 1 : 0;
    count += pathSumStartWithRoot(root->left, sum - root->val);
    count += pathSumStartWithRoot(root->right, sum - root->val);
    return count;
}

int pathSum(TreeNode* root, int sum) {
    return root ? pathSumStartWithRoot(root, sum) +
    pathSum(root->left, sum) + pathSum(root->right, sum) : 0;
}

bool isSymmetric(TreeNode* left, TreeNode* right) {
    if (!left && !right) {
        return true;
    }
    if (!left || !right) {
        return false;
    }
    if (left->val != right->val) {
        return false;
    }
    return isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left);
}

bool isSymmetric(TreeNode *root) {
    return root ? isSymmetric(root->left, root->right) : true;
}

TreeNode* helper(TreeNode* root, unordered_set<int>& dict, vector<TreeNode*>& forest) {
    if (!root) {
        return root;
    }
    root->left = helper(root, dict, forest);
    root->right = helper(root, dict, forest);
    if (dict.count(root->val)) {
        if (root->left) {
            forest.push_back(root->left);
        }
        if (root->right) {
            forest.push_back(root->right);
        }
        root = NULL;
    }
    return root;
}

vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
    vector<TreeNode*> forest;
    unordered_set<int> dict(to_delete.begin(), to_delete.end());
    root = helper(root, dict, forest);
    if (root) {
        forest.push_back(root);
    }
    return forest;
}

vector<double> averageOfLevels(TreeNode* root) {
    vector<double> ans;
    if (!root) {
        return ans;
    }
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int count = q.size();
        double sum = 0;
        for (int i = 0; i < count; ++i) {
            TreeNode* node = q.front();
            q.pop();
            sum += node->val;
            if (node->left) {
                q.push(node->left);
            }
            if (node->right) {
                q.push(node->right);
            }
        }
        ans.push_back(sum / count);
    }
    return ans;
}

vector<int> preorderTraversal(TreeNode* root) {
    vector<int> ret;
    if (!root) {
        return ret;
    }
    stack<TreeNode*> s;
    s.push(root);
    while (!s.empty()) {
        TreeNode* node = s.top();
        s.pop();
        ret.push_back(node->val);
        if (node->right) {
            s.push(node->right);// 先右后左，保证左子树先遍历
        }
        if (node->left) {
            s.push(node->left);
        }
    }
    return ret;
}

void printAllString(char* str) {
    int length = strlen(str);
    if (!length) {
        return;
    }
    if (length > 100) {
        cout << "字符串长度不能大于100" << endl;
        return;
    }
    int size = 8;
    char* pStr = str;
    int stringSize = 0;
    int yuCount = length % size;
    // int stringCount = length % size == 0 ? length / size : length / size + 1;
    while (*pStr != '\0') {
        stringSize++;
        if (stringSize % size == 0) {
            printf("%c", '\n');
            printf("%c", *pStr);
        } else {
            printf("%c", *pStr);
        }
        pStr++;
    }
    for (int i = 0; i < size - yuCount; ++i) {
        printf("%c", '0');
    }
    
}

```

## 最低公共祖先

```

unsigned int GetListLength(ListNode* pHead) {
    unsigned int nLength = 0;
    ListNode* pNode = pHead;
    while (pNode != NULL) {
        ++nLength;
        pNode = pNode->m_pNext;
    }
    return nLength;
}

ListNode* FindFirstCommonNode(ListNode* pHead1, ListNode* pHead2) {
    // 得到两个链表的长度
    unsigned int nLength1 = GetListLength(pHead1);
    unsigned int nLength2 = GetListLength(pHead2);
    int nLengthDif = nLength1 - nLength2;
    
    ListNode* pListHeadLong = pHead1;
    ListNode* pListHeadShort = pHead2;
    if (nLength2 > nLength1) {
        pListHeadLong = pHead2;
        pListHeadShort = pHead1;
        nLengthDif = nLength2 - nLength1;
    }
    
    // 先在长链表上走几步，再同时在两个链表上遍历
    for (int i = 0; i < nLengthDif; ++i) {
        pListHeadLong = pListHeadLong->m_pNext;
    }
    
    while ((pListHeadLong != NULL) && (pListHeadShort != NULL) && (pListHeadLong != pListHeadShort)) {
        pListHeadLong = pListHeadLong->m_pNext;
        pListHeadShort = pListHeadShort->m_pNext;
    }
    
    // 得到第一个公共结点
    ListNode* pFirstCommondNode = pListHeadLong;
    
    return pFirstCommondNode;
}

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    vector<TreeNode*> m_vChildren;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};



// 最低公共祖先
bool GetNodePath(TreeNode* pRoot, TreeNode* pNode, list<TreeNode*>& path) {
    if (pRoot == pNode) {
        return true;
    }
    path.push_back(pRoot);
    
    bool found = false;
    
    vector<TreeNode*>::iterator i = pRoot->m_vChildren.begin();
    while (!found && i < pRoot->m_vChildren.end()) {
        found = GetNodePath(*i, pNode, path);
        ++i;
    }
    
    if (!found) {
        path.pop_back();
    }
    
    return found;
}

TreeNode* GetLastCommonNode(const list<TreeNode*>& path1, const list<TreeNode*>& path2) {
    list<TreeNode*>::const_iterator iterator1 = path1.begin();
    list<TreeNode*>::const_iterator iterator2 = path2.begin();
    
    TreeNode* pLast = NULL;
    while (iterator1 != path1.end() && iterator2 != path2.end()) {
        if (*iterator1 == *iterator2) {
            pLast = *iterator1;
        }
        iterator1++;
        iterator2++;
    }
    
    return pLast;
}

TreeNode* GetLastCommonParent(TreeNode* pRoot, TreeNode* pNode1, TreeNode* pNode2) {
    if (pRoot == NULL || pNode1 == NULL || pNode2 == NULL) {
        return NULL;
    }
    
    list<TreeNode*> path1;
    GetNodePath(pRoot, pNode1, path1);
    
    list<TreeNode*> path2;
    GetNodePath(pRoot, pNode2, path2);
    
    return GetLastCommonNode(path1, path2);
}

```

## 合并两个排序的链表

```

ListNode* Merge(ListNode* pHead1, ListNode* pHead2) {
    if (pHead1 == NULL) {
        return pHead2;
    } else if (pHead2 == NULL) {
        return pHead1;
    }
    
    ListNode* pMergedHead = NULL;
    if (pHead1->m_nValue < pHead2->m_nValue) {
        pMergedHead = pHead1;
        pMergedHead->m_pNext = Merge(pHead1->m_pNext, pHead2);
    } else {
        pMergedHead = pHead2;
        pMergedHead->m_pNext = Merge(pHead1, pHead2->m_pNext);
    }
    return pMergedHead;
}

```

## 跳表 

链表加多级索引的结构，就是跳表。

### 用跳表查询到底有多快？
第 k 级索引的结点个数是第 k-1 级索引的结点个数的 1/2，那第 k级索引结点的个数就是 n/(2k)。

时间复杂度： O(m*logn)。

### 跳表是不是很浪费内存？
跳表需要存储多级索引，肯定要消耗更多的存储空间。

跳表的空间复杂度是 O(n)。

### 为什么 Redis 要用跳表来实现有序集合，而不是红黑树？
Redis 中的有序集合支持的核心操作主要有下面这几个：
```
插入一个数据；

删除一个数据；

查找一个数据；

按照区间查找数据（比如查找值在 [100, 356] 之间的数据）；

迭代输出有序序列。
```
其中，插入、删除、查找以及迭代输出有序序列这几个操作，红黑树也可以完成，时间复杂度跟跳表是一样的。但是，`按照区间来查找数据这个操作，红黑树的效率没有跳表高`。

对于按照区间查找数据这个操作，跳表可以做到 O(logn) 的时间复杂度定位区间的起点，然后在原始链表中顺序往后遍历就可以了。这样做非常高效。

还有，跳表更加灵活，它可以通过改变索引构建策略，有效平衡执行效率和内存消耗。

## 图

### 一、图的定义
```
图(Graph)是由顶点的有穷非空集合V ( G ) 和顶点之间边的集合E ( G )组成，通常表示为: G = ( V , E ) ，其中，G表示个图，V 是图G中顶点的集合，E是图G中边的集合。若V = { v 1 , v 2 , . . . , v n } ，则用∣ V ∣表示图G中顶点的个数，也称图G的阶，E = { ( u , v ) ∣ u ∈ V , v ∈ V } ，用∣ E ∣表示图G中边的条数。

注意:线性表可以是空表，树可以是空树，但图不可以是空图。就是说，图中不能一个顶点也没有，图的顶点集V一定非空，但边集E可以为空，此时图中只有顶点而没有边。

```

### 二、图的基本概念和术语
  1、有向图
若E是有向边(也称弧)的有限集合时，则图G为有向图。弧是顶点的有序对，记为<v, w>，其中v,w是顶点，v称为弧尾，w称为弧头，<v,w>称为从顶点v到顶点w的弧，也称v邻接到w，或w邻接自v。

### 图的存储


### 拓扑排序


### 最短路径


### 关键路径


### 最小生成树


### 二分图

`未完待续。。。`


## 以下代码是在Xcode环境编译运行的
```
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <cassert>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include "TemplateDemo.hpp"
#include <exception>
#include <pthread.h>

typedef struct {
    pthread_mutex_t mutex; // Mutex to protect access to the structure
    char *name;
    void **ptr;
    size_t bufsize;
    int freetotal;
    int freecurr;
    
}cache_t;

using namespace std;

#ifndef NDEBUG
const uint64_t redzone_pattern = 0xdeadbeefcafebabe;
int cache_error = 0;
#endif

const int initial_pool_size = 64;

cache_t* cache_create(const char *name, size_t bufsize, size_t align) {
    cache_t *ret = (cache_t *)calloc(1, sizeof(cache_t));
    char* nm = strdup(name);
    void **ptr = (void **)calloc(initial_pool_size, sizeof(void *));
    if (ret == NULL || nm == NULL || ptr == NULL || pthread_mutex_init(&ret->mutex, NULL) == -1) {
        free(ret);
        free(nm);
        free(ptr);
        return NULL;
    }
    
    ret->name = nm;
    ret->ptr = ptr;
    ret->freetotal = initial_pool_size;
#ifndef NDEBUG
    ret->bufsize = bufsize + 2 * sizeof(redzone_pattern);
#else
    ret->bufsize = bufsize;
#endif
    
    return ret;
}

class Solution
{
public:
    // ip字符串输入默认采用IPV4的点分十进制法，合法地址为0.0.0.0-255.255.255.255
    bool isLegalIP(const string& ip)
    {
        int validSegSize = 0; // 记录一共有多少个分段
        
        int oneSeg = 0; // 记录每个分段的数值
        int segLen = 0; // 记录是否分段有数值
        for (int i = 0; i < ip.length(); ++i)
        {
            // 计算每个分段的数值
            if (ip[i] >= '0' && ip[i] <= '9')
            {
                oneSeg = oneSeg * 10 + (ip[i] - '0');
                // 如果分段有数值，就置segLen为1
                ++segLen;
            }
            else if (ip[i] == '.') // 如果此字符为'.'，那么就判断之前的那个分段的值是否合法且是否存在值
            {
                if (oneSeg <= 255 && segLen > 0)
                    validSegSize++;
                else
                    return false;
                
                oneSeg = 0; // 重置分段值
                segLen = 0; // 重置分段是否存在值
            }
            else // 如果出现0-9或'.'以外的字符都判断为非法
                return false;
        }
        
        // 判断最后一个分段的合法性
        if (oneSeg <= 255 && segLen > 0)
            validSegSize++;
        
        // 判断是否一共有四个分段
        if (validSegSize == 4)
            return true;
        else
            return false;
    }
    
    bool isLegalIP2(const string& ip)
    {
        int validSegSize = 0;
        
        int oneSeg = 0;
        int segLen = 0;
        for (int i = 0; i < ip.length(); ++i) {
            if (ip[i] >= '0' && ip[i] <= '9') {
                oneSeg = oneSeg * 10 + (ip[i] - '0');
                ++segLen;
            } else if (ip[i] == '.') {
                if (oneSeg <= 255 && segLen > 0) {
                    validSegSize++;
                } else {
                    return false;
                }
                oneSeg = 0;
                segLen = 0;
            } else {
                return false;
            }
        }
        if (oneSeg <= 255 && segLen > 0) {
            validSegSize++;
        }
        if (validSegSize == 4) {
            return true;
        } else {
            return false;
        }
    }
};

bool findMatrix(int *martix, int rows, int columns, int number);
// 二维数组中的查找
bool findMatrix(int *martix, int rows, int columns, int number)
{
    bool found = false;
    if (martix != NULL && rows > 0 && columns > 0) {
        int row = 0;
        int column = columns - 1;
        while (row < rows && column >= 0) {
            if (martix[row * columns + column] == number) {
                found = true;
                break;
            }
            else if (martix[row * columns + column] > number)
                --column;
            else
                ++row;
        }
    }
    return found;
}

bool findMatrix2(int *martix, int rows, int columns, int number)
{
    bool found = false;
    if (martix != NULL && rows > 0 && columns > 0) {
        int row = 0;
        int column = columns - 1;
        while (row < rows && column >= 0) {
            if (martix[row * columns + column] == number) {
                found = true;
                break;
            } else if (martix[row * columns + column] > number) {
                --column;
            } else {
                ++row;
            }
        }
    }
    return found;
}

// 空格的替换
/*length为字符数组string替换后的总容量*/
void ReplaceBlank(char string[], int length)
{
    if (string == NULL && length <= 0) {
        return;
    }
    /*originalLength为字符串string的实际长度*/
    int originalLength = 0;
    int numberOfBlank = 0;
    int i = 0;
    while (string[i] != '\0') {
        ++originalLength;
        if (string[i] == ' ') {
            ++numberOfBlank;
        }
        ++i;
    }
    /*newLength为把空格替换成'%20'之后的长度*/
    int newLength = originalLength + numberOfBlank * 2;
    if (newLength > length) {
        return;
    }
    int indexOfOriginal = originalLength;
    int indexOfNew = newLength;
    while (indexOfOriginal >= 0 && indexOfNew > indexOfOriginal) {
        if (string[indexOfOriginal] == ' ') {
            string[indexOfNew--] = '0';
            string[indexOfNew--] = '2';
            string[indexOfNew--] = '%';
        }
        else {
            string[indexOfNew--] = string[indexOfOriginal];
        }
        --indexOfOriginal;
    }
}

struct BinaryTreeNode {
    int m_nValue;
    BinaryTreeNode *m_pLeft;
    BinaryTreeNode *m_pRight;
};

/*重建二叉树*/
BinaryTreeNode *ConstructCore(int *startPreorder, int *endPreorder, int *startInorder, int *endInorder)
{
    // 前序遍历序列的第一个数字是根结点的值
    int rootValue = startPreorder[0];
    BinaryTreeNode *root = new BinaryTreeNode();
    root->m_nValue = rootValue;
    root->m_pLeft = root->m_pRight = NULL;
    
    if (startPreorder == endPreorder) {
        if (startInorder == endInorder && *startPreorder == *startInorder) { // 只有一个结点的情况并判断两种遍历序列是否匹配
            return root;
        }
        else {
//            throw std::exception("Invalid input");
        }
    }
    // 在中序遍历中找到根结点的值
    int *rootInorder = startInorder;
    while (rootInorder <= endInorder && *rootInorder != rootValue) {
        ++rootInorder;
    }
    if (rootInorder == endInorder && *rootInorder != rootValue) { //
//        throw std::exception("Invalid input.");
    }
    long leftLength = rootInorder - startInorder;
    int *leftPreorderEnd = startPreorder + leftLength;
    if (leftLength > 0) {
        // 构建左子树
        root->m_pLeft = ConstructCore(startPreorder+1, leftPreorderEnd, startInorder, rootInorder-1);
    }
    if (leftLength < endPreorder - startPreorder) {
        // 构建右子树
        root->m_pRight = ConstructCore(leftPreorderEnd+1, endPreorder, rootInorder+1, endInorder);
    }
    return root;
}

BinaryTreeNode *Construct(int *preoder, int *inorder, int length)
{
    if (preoder == NULL || inorder == NULL || length <= 0) { // 判断二叉树的根结点指针为NULL情况
        return NULL;
    }
    return ConstructCore(preoder, preoder + length - 1, inorder, inorder + length - 1);
}

struct BinaryTreeNode2 {
    int m_nValue;
    BinaryTreeNode2 *m_pLeft;
    BinaryTreeNode2 *m_pRight;
};


typedef struct LNode{
    int data;
    struct LNode *prior;
    struct LNode *next;
}LNode, *DLinkList;

int StrToInt(char *string)
{
    int number = 0;
    while (*string != 0) {
        number = number * 10 + *string - '0';
        ++string;
    }
    return number;
}

#define is_digit(a) ((a) >= '0' && (a) <= '9')
#define is_space(a) ((a) == ' ' || (a) == '\t')

int atoi(char* s) {
    if(!s || !*s) return 0;
    while(is_space(*s)) ++s;
    
    int sign = *s != '-';
    if(*s == '+' || *s == '-') ++s;
    if(!is_digit(*s)) return 0;
    
    unsigned v = *s - '0', upper = sign > 0 ? INT_MAX : INT_MIN;;
    while(*++s && is_digit(*s)){
        if(v > upper/10 || (v = v * 10  + (*s-'0')) > upper){
            return sign ? INT_MAX : INT_MIN;
        }
    }
    return sign ? v : -v;
}

// atoi字符串转整型函数 考虑到各种特殊的输入 譬如：输入的字符串中有非数字字符和正负号，要考虑到最大的正整数和最小的负整数以及溢出。当输入的字符串不能转换成整数时，如何做错误处理。对空指针判断并加以特殊处理
/*
int atoi(const char *str)
{
    if(str == NULL)
        return 0;
    const char *p = str;
    char c;
    int i = 0;
    
    if (*str == '-' || *str == '+') { // 如果第一个字符是正负号
        // 则移到下一个字符
        str++;
    }
    
    while ((c = *str++)) {
        if(c >= '0' && c <= '9') {
            i = i * 10 + (c - '0');
        }
        else
            break;
    }
    if (*p == '-') {
        i = -i;
    }
    
    return i;
}
 */

// 用两个栈实现一个队列。 题目：用两个栈实现一个队列。队列的生命如下，请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。

template <typename T> class CQueue
{
public:
    CQueue(void);
    ~CQueue(void);
    void appendtail(const T& node);
    T deleteHead();
private:
    stack<T> stack1;
    stack<T> stack2;
};

// 构造函数
template <typename T> CQueue<T>::CQueue(void)
{
}

// 析构函数
template <typename T> CQueue<T>::~CQueue(void)
{
}

// 插入元素
template <typename T> void CQueue<T>::appendtail(const T& node)
{
    stack1.push(node);
}

// 删除元素并返回
template <typename T> T CQueue<T>::deleteHead()
{
    if(stack2.size()<=0)
    {
        while(stack1.size()>0)
        {
            stack2.push(stack1.top());
            stack1.pop();
        }
    }
    if(stack2.size()==0)
        cout<<"队列为空"<<endl;
//        throw new exception("队列为空");
    T head=stack2.top();
    stack2.pop();
    return head;
}

// 使用两个队列实现一个栈
//解法：

//有两个队列q1和q2，先往q1内插入a，b，c，这做的都是栈的push操作。
//现在要做pop操作，即要得到c，这时可以将q1中的a,b两个元素全部dequeue并存入q2中，这时q2中元素为a，b，对q1再做一次dequeue操作即可得到c。
//如果继续做push操作，比如插入d，f，则把d，f插入到q2中，
//此时若要做pop操作，则做步骤2
//以此类推，就实现了用两个队列来实现一个栈的目的。
//注意在此过程中，新push进来的元素总是插入到非空队列中，空队列则用来保存pop操作之后的那些元素，那么此时空队列不为空了，原来的非空队列变为空了，总是这样循环。

//对于push和pop操作，其时间为O(n).

template <typename T>class CStack
{
public:
    CStack(void){};
    ~CStack(void){};
    void push(const T& node);
    T pop();
private:
    queue<T> queue1;
    queue<T> queue2;
    
};

//插入元素
template <typename T> void CStack<T>::push(const T& element)
{
    if(queue1.size()>0)     // 如果queue1不为空则往queue1中插入元素
        queue1.push(element);
    else if(queue2.size()>0)// 如果queue2不为空则往queue2中插入元素
        queue2.push(element);
    else                    // 如果两个队列都为空，则往queue1中插入元素
        queue1.push(element);
    
}

// 删除元素
template <typename T> T CStack<T>::pop()
{
    if(queue1.size()==0)// 如果queue1为空
    {
        while(queue2.size()>1)// 保证queue2中有一个元素，将其余元素保存到queue1中
        {
            queue1.push(queue2.front());
            queue2.pop();
        }
        T& data=queue2.front();
        queue2.pop();
        return data;
    }
    else// 如果queue2为空
    {
        while(queue1.size()>1)// 保证queue2中有一个元素，将其余元素保存到queue1中
        {
            queue2.push(queue1.front());
            queue1.pop();
        }
        T& data=queue1.front();
        queue1.pop();
        return data;
    }
    
}

//// memcpy内存拷贝函数实现
//void *memcpy(void *dest, const void *src, size_t count)
//{
//    assert(dest != NULL && src != NULL);
//    char *tmp = (char *)dest;
//    const char *s = (const char *)src;
//    while (count--) {
//        *tmp++ = *s++;
//    }
////    while ((*tmp++ = *s++) != '\0');
//    return dest;
//}

char *strcpy(char *strDest, const char *strSrc) // 实现strSrc到strDest的复制
{
    if ((strDest == NULL) || (strSrc == NULL)) //判断参数strDest和strSrc的有效性
    {
        return NULL;
    }
    char *strDestCopy = strDest;        //保存目标字符串的首地址
    while ((*strDest++ = *strSrc++)!='\0'); //把strSrc字符串的内容复制到strDest下
    
    return strDestCopy;
}

// 请写出双向链表的删除目标值nVal的方法，并输出删除数量
DLinkList DLinkListDelete(DLinkList L,int i)
{
    int tempi = 1;
    DLinkList p; //p为查找结点。
    p = L->next;
    while((tempi++) != i && p != NULL)
    {
        p = p->next;
    }
    //检查是不是在双链表中的位置
    if(p == NULL)  printf("位置不合法。\n");
    else if(p->next == NULL) //最后一个结点特殊处理，原因最后一个结点p->next没有prior
    {
        p->prior->next = NULL;
        free(p);
    }
    else //进行删除操作
    {
        p->prior->next = p->next;
        p->next->prior = p->prior;
        free(p);
    }
    return L;
}

//链表结构
struct ListNode
{
    int m_nValue;
    ListNode* m_pNext;
};

//创建一个链表结点
ListNode* CreateListNode(int value)
{
    ListNode *pNode=new ListNode();
    pNode->m_nValue=value;
    pNode->m_pNext=NULL;
    return pNode;
    
}

//遍历链表中的所有结点
void PrintList(ListNode* pHead)
{
    ListNode *pNode=pHead;
    while(pNode!=NULL)
    {
        cout<<pNode->m_nValue<<" ";
        pNode=pNode->m_pNext;
    }
    cout<<endl;
}

//往链表末尾添加结点
/*
 注意这里pHead是一个指向指针的指针，在主函数中一般传递的是引用。
 因为如果要为链表添加结点，那么就会修改链表结构，所以必须传递引用才能够保存修改后的结构。
 */
void AddToTail(ListNode** pHead,int value)
{
    ListNode* pNew=new ListNode();//新插入的结点
    pNew->m_nValue=value;
    pNew->m_pNext=NULL;
    
    if(*pHead==NULL)//空链表
    {
        *pHead=pNew;
    }
    else
    {
        ListNode* pNode=*pHead;
        while(pNode->m_pNext!=NULL)
            pNode=pNode->m_pNext;
        pNode->m_pNext=pNew;
    }
    
}

ListNode* ReverseList(ListNode* pHead)
{
    if (pHead == NULL || pHead->m_pNext == NULL)
        return pHead;
    ListNode* pNode=pHead;//当前结点
    ListNode* pPrev=NULL;//当前结点的前一个结点
    ListNode* pReversedHead=NULL;//反转链表头结点
    while(pNode!=NULL)
    {
        ListNode* pNext=pNode->m_pNext;
        if(pNext==NULL)//如果当前结点的下一个结点为空，那么反转链表的头结点就是当前结点。
            pReversedHead=pNode;
        
        pNode->m_pNext=pPrev;//当前结点指向前一个结点
        
        pPrev=pNode;//pPrev和pNode往前移动。
        pNode=pNext;//这里要使用前面保存下来的pNext，不能使用pNode->m_pNext
    }
    return pReversedHead;//返回反转链表头指针。
}

ListNode* ReverseList2(ListNode* pHead)
{
    ListNode* pNode=pHead;//当前结点
    ListNode* pPrev=NULL;//当前结点的前一个结点
    while(pNode!=NULL)
    {
        ListNode* pNext=pNode->m_pNext;
        pNode->m_pNext=pPrev;//当前结点指向前一个结点
        
        pPrev=pNode;//pPrev和pNode往前移动。
        pNode=pNext;//这里要使用前面保存下来的pNext，不能使用pNode->m_pNext
    }
    return pPrev;//返回反转链表头指针。
}

ListNode * ReverseList_Digui(ListNode* pHead,ListNode* pHead2 = NULL)
{
    if(pHead == NULL)
        return pHead2;
    ListNode * pTemp = pHead->m_pNext;
    pHead->m_pNext = pHead2;
    return ReverseList_Digui(pTemp,pHead);
}

// 创建二叉树结点
BinaryTreeNode *CreateBinaryTreeNode(int value)
{
    BinaryTreeNode *pNode = new BinaryTreeNode;
    pNode->m_pLeft = NULL;
    pNode->m_pRight = NULL;
    pNode->m_nValue = value;
    return pNode;
}

void ConnectTreeNodes(BinaryTreeNode *pParent, BinaryTreeNode *pLeft, BinaryTreeNode *pRight)
{
    if (pParent != NULL) {
        pParent->m_pLeft = pLeft;
        pParent->m_pRight = pRight;
    }
}

void InOrderPrintTree(BinaryTreeNode *pRoot)
{
    cout<<"调用"<<pRoot<<endl;
    // 中序遍历
    if (pRoot != NULL) {
        if (pRoot->m_pLeft != NULL) {
            InOrderPrintTree(pRoot->m_pLeft);
        }
        cout<<"value of this node is "<<pRoot->m_nValue<<endl;
        if (pRoot->m_pRight != NULL) {
            InOrderPrintTree(pRoot->m_pRight);
        }
    }
    else {
        cout<<"this node is null."<<endl;
    }
}

// 在转换成排序双向链表时，原先指向左子结点的指针调整为链表中指向前一个结点的指针，原先指向右子树结点的指针调整为链表中指向后一个结点指针。

void ConvertNode(BinaryTreeNode *pNode,BinaryTreeNode **pLastNodeInList)
{
    if (pNode == NULL) {
        return;
    }
    
    BinaryTreeNode *pCurrent = pNode;
    // 左子树转换，遍历到左子树的叶子结点
    if (pCurrent->m_pLeft != NULL) {
        // 遍历左子树
        ConvertNode(pCurrent->m_pLeft, pLastNodeInList);
    }
    
    pCurrent->m_pLeft = *pLastNodeInList;
    if ((*pLastNodeInList) != NULL) {
        (*pLastNodeInList)->m_pRight = pCurrent;
    }
    
    *pLastNodeInList = pCurrent;
    // 右子树转换
    if (pCurrent->m_pRight != NULL) {
        // 遍历右子树
        ConvertNode(pCurrent->m_pRight, pLastNodeInList);
    }
}

// 转换左子树和右子树
BinaryTreeNode *Convert(BinaryTreeNode *pRootOfTree)
{
    BinaryTreeNode *pLastNodeInList = NULL;     // 指向双向链表的尾接点
    ConvertNode(pRootOfTree, &pLastNodeInList); // 转换排序二叉树为双向链表
    
    // 求双向链表的头结点,我们需要返回头结点
    BinaryTreeNode *pHeadOfList = pLastNodeInList;
    while (pHeadOfList != NULL && pHeadOfList->m_pLeft != NULL) {
        pHeadOfList = pHeadOfList->m_pLeft;
    }
    return pHeadOfList;
}

// 输出双向链表
void PrintList(BinaryTreeNode *pRoot)
{
    BinaryTreeNode *pNode = pRoot;
    while (pNode != NULL) {
        printf("%d\t", pNode->m_nValue);
        pNode = pNode->m_pRight;
    }
    printf("\nPrintList ends.\n");
}

// 二叉搜索树的后序遍历序列 Binary Search Tree
bool VerifySequenceOfBST(int sequence[], int length)
{
    if (sequence == NULL || length <= 0) {
        return false;
    }
    
    int root = sequence[length - 1];
    
    // 在二叉搜索树中左子树的结点小于根节点
    int i = 0;
    for (; i < length - 1; ++i) {
        if (sequence[i] > root) {
            break;
        }
    }
    // 在二叉搜索树中右子树的结点大于根结点
    int j = i;
    for (; j < length - 1; ++j) {
        if (sequence[j] < root) {
            return false;
        }
    }
    // 判断左子树是不是二叉搜索树
    bool left = true;
    if (i > 0) {
        left = VerifySequenceOfBST(sequence, i);
    }
    // 判断右子树是不是二叉搜索树
    bool right = true;
    if (i < length - 1) {
        right = VerifySequenceOfBST(sequence + i, length - i - 1);
    }
    
    return (left && right);
}

int lengthOfLongestSubstring(string s) {
    int size, i = 0, j, k, max = 0;
    size = s.size();
    for (j = 0; j < size; j++) {
        for (k = i; k < j; k++) {
            if (s[k] == s[j]) {
                i = k + 1;
                break;
            }
        }
        if (j - i + 1 > max) {
            max = j - i + 1;
        }
    }
    return max;
}

template <typename AnyType>

inline void Swap(AnyType &a, AnyType &b)
{
    AnyType temp;
    temp = a;
    a = b;
    b = temp;
}

// 全排列
void Permutation(char string[], int start, size_t end)
{
    if (string == NULL) {
        return;
    }
    if(start == end) {
        cout<<string<<endl;
    }
    else {
        for (int i = start; i <= end; i++) {
            Swap(string[i], string[start]);
            Permutation(string, start+1, end);
            Swap(string[i], string[start]);
        }
    }
}

void Permutation(char *pStr, char *pBegin)
{
    if (*pBegin == '\0') {
        printf("%s\n", pStr);
    }
    else {
        for (char *pCh = pBegin; *pCh != '\0'; ++pCh) {
            char temp = *pCh;
            *pCh = *pBegin;
            *pBegin = temp;
            
            Permutation(pStr, pBegin + 1);
            
            temp = *pCh;
            *pCh = *pBegin;
            *pBegin = temp;
        }
    }
}

void Permutation(char *pStr)
{
    if (pStr == NULL) {
        return;
    }
    Permutation(pStr, pStr);
}

bool fun2(int b, int c, int *a)
{
    return true;
}

const int *fun(int x, int y)
{
    int b = x+y;
    int *c = &b;
    
    return c;
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

/*生成一个在start和end之间的随机数*/
int RandomInRange(int start, int end)
{
    int rand = static_cast<int>(random());
    do {
        rand = static_cast<int>(random());
    } while (rand > start && rand < end);
    return rand;
}

// 快速排序算法的关键在于先在数组中选择一个数字，接下来把数组中的数字分为两部分，比选择的数字小的数字移到数组的左边，比选择的数字大的数字移到数组的右边
int Partition(int data[], int length, int start, int end)
{
    if (data == NULL || length <= 0 || start < 0 || end >= length) {
        //        throw new std::exception("Invalid Parameters");
        return -1;
    }
    int index = RandomInRange(start, end);
    swap(&data[index], &data[end]);
    
    int small = start - 1;
    for (index = start; index < end; ++index) {
        if (data[index] < data[end]) {
            ++small;
            if (small != index) {
                swap(&data[index], &data[small]);
            }
        }
    }
    ++small;
    swap(&data[small], &data[end]);
    
    return small;
}

void QuickSort(int data[], int length, int start, int end)
{
    if (start == end) {
        return;
    }
    int index = Partition(data, length, start, end);
    if (index > start) {
        QuickSort(data, length, start, index - 1);
    }
    if (index < end) {
        QuickSort(data, length, index + 1, end);
    }
}

void Qsort(int a[], int low, int high)
{
    cout<<"循环一次"<<endl;
    if(low >= high)
    {
        return;
    }
    int first = low;
    int last = high;
    int key = a[first];/*用字表的第一个记录作为枢轴*/
    
    while(first < last)
    {
        while(first < last && a[last] >= key)
        {
            --last;
        }
        
        a[first] = a[last];/*将比第一个小的移到低端*/
        
        while(first < last && a[first] <= key)
        {
            ++first;
        }
        
        a[last] = a[first];
        /*将比第一个大的移到高端*/
    }
    a[first] = key;/*枢轴记录到位*/
    Qsort(a, low, first-1);
    Qsort(a, first+1, high);
}

void SortAges(int ages[], int length)
{
    if (ages == NULL || length <= 0) {
        return;
    }
    const int oldestAge = 99;
    int timesOfAge[oldestAge+1];
    for (int i = 0; i <= oldestAge; i++) {
        timesOfAge[i] = 0;
    }
    for (int i = 0; i < length; i++) {
        int age = ages[i];
        if (age > oldestAge || age < 0) {
//            throw new std::exception("age out of range.");
        }
        ++timesOfAge[age];
        cout<<"age为"<<age<<"的次数为:"<<timesOfAge[age]<<endl;
    }
    
    int index = 0;
    for (int i = 0; i <= oldestAge; i++) {
        for (int j = 0; j < timesOfAge[i]; j++) {
            ages[index] = i;
            index++;
        }
    }
}

// 旋转数组的最小数字 二分查找
int MinInOrder(int *numbers, int index1, int index2)
{
    int result = numbers[index1];
    for (int i = index1 + 1; i <= index2; i++) {
        if (result > numbers[i]) {
            result = numbers[i];
        }
    }
    return result;
}

int MinNumber(int *numbers, int length) // 考查思维的全面性。排序数组本身是数组旋转的一个特例。另外考虑数组中有相同数字的特例
{
    if (numbers == NULL || length <= 0) {
//        throw new std::exception("Invalid parameters");
    }
    int index1 = 0;
    int index2 = length - 1;
    int indexMid = index1; // 之所以把indexMid初始化为index1，是因为有特例，如果把排序数组的前面0个元素搬到最后面，即排序数组本身，这仍然是数组的一个旋转，
    while (numbers[index1] >= numbers[index2]) {
        if (index2 - index1 == 1) {
            indexMid = index2;
            break;
        }
        indexMid = (index1 + index2) / 2;
        // 如果下标为index1、index2和indexMid指向的三个数字相等，则只能顺序查找
        if (numbers[index1] == numbers[index2] && numbers[indexMid] == numbers[index1]) {
            return MinInOrder(numbers, index1, index2);
        }
        
        if (numbers[indexMid] >= numbers[index1]) {
            index1 = indexMid;
        }
        else if (numbers[indexMid] <= numbers[index2]) {
            index2 = indexMid;
        }
    }
    return numbers[indexMid];
}

// 递归
int AddFrom1ToN_Recursive(int n)
{
    return n <= 0 ? 0 : n + AddFrom1ToN_Recursive(n - 1);
}

int AddFrom1ToN_Iterative(int n)
{
    int result = 0;
    for (int i = 1; i <= n; i++) {
        result += i;
    }
    return result;
}

long long Fibonacci(unsigned n) // 第三种方法 转换成求矩阵的乘方
{
    int result[2] = {0, 1};
    if (n < 2) {
        return result[n];
    }
    long long fibNMinusOne = 1;
    long long fibNMinusTwo = 0;
    long long fibN = 0;
    for (unsigned int i = 2; i <= n; ++i) {
        fibN = fibNMinusOne + fibNMinusTwo;
        fibNMinusTwo = fibNMinusOne;
        fibNMinusOne = fibN;
    }
    return fibN;
}

// 二进制中1的个数
int NumberOf1(int n) // 右移考虑负数，当为负数，最高位为1，导致出现0xFFFFFFFF进入死循环
{
    int count = 0;
    unsigned int flag = 1; // 复杂度为o(n),有多少个位数就得循环多少次
    while (flag) {
        if (n & flag) {
            count++;
        }
        flag = flag << 1;
    }
    return count;
}

// 把一个整数1100减去1得到1011，再和原整数做与运算得到1000，会把该整数最右边一个1变成0.那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。
int NumberOf1InBinary(int n) // 1.一个整数如果是2的整数次方，那么它的二进制表示中有且只有一位是1，其他位都是0.把整数减去1之后再和它自己做与运算 ，这个整数中唯一的1就会变成0.      2.输入两个整数m和n,计算需要改变m的二进制表示中的多少位才能得到0.第一步求这两个数的异或，第二步统计异或结果中1的位数。 举一反三：把一个整数减去1之后再和原整数做位与运算，得到的结果相当于是把整数的二进制表示中的最右边一个1变成0.
{
    int count = 0;
    while (n) {
        ++count;
        n = (n - 1) & n;
    }
    return count;
}

// 基数的几次方
bool equal(double num1, double num2)
{
    if ((num1 - num2 > -0.0000001) && (num1 - num2 < 0.0000001)) {
        return true;
    }
    else {
        return false;
    }
}

double PowerWithUnsignedExponent(double base, unsigned int exponent) // 左移
{
    /*
    double result = 1.0;
    for (int i = 1; i <= exponent; ++i) {
        result *= base;
    }
    return result;
     */
    if (exponent == 0) {
        return 1;
    }
    if (exponent == 1) {
        return base;
    }
    
    double result = PowerWithUnsignedExponent(base, exponent >> 1);
    result *= result;
    if ((exponent & 0x1) == 1) { // 判断是否是奇数，如果是奇数，则需要再一次乘以基数base。位与运算代替了求余运算符%来判断一个数是奇数还是偶数。
        result *= base;
    }
    return result;
}

bool g_InvalidInput = false;

double Power(double base, int exponent)
{
    g_InvalidInput = false;
    if (equal(base, 0.0) && exponent < 0) {
        g_InvalidInput = true;
        return 0.0;
    }
    
    unsigned int absExponent = (unsigned int)(exponent);
    if (exponent < 0) {
        absExponent = (unsigned int)(-exponent);
    }
    double result = PowerWithUnsignedExponent(base, absExponent);
    if (exponent < 0) {
        result = 1.0 / result;
    }
    return result;
}

bool Increment(char *number)
{
    bool isOverflow = false;
    int nTakeOver = 0;
    int nLength = static_cast<int>(strlen(number));
    for (int i = nLength - 1; i >= 0; i--) {
        int nSum = number[i] - '0' + nTakeOver;
        if (i == nLength - 1) {
            nSum++;
        }
        if (nSum >= 10) {
            if (i == 0) {
                isOverflow = true;
            }
            else {
                nSum -= 10;
                nTakeOver = 1;
                number[i] = '0' + nSum;
            }
        }
        else {
            number[i] = '0' + nSum;
            break;
        }
    }
    return isOverflow;
}

void PrintNumber(char *number)
{
    bool isBeginning0 = true;
    int nLength = static_cast<int>(strlen(number));
    for (int i = 0; i < nLength; i++) {
        if (isBeginning0 && number[i] != '0') {
            isBeginning0 = false;
        }
        if (!isBeginning0) {
            printf("%c", number[i]);
        }
    }
    printf("\t");
}

void Printf1ToMaxOfDigitsRecursively(char *number, int length, int index)
{
    if (index == length - 1) {
        PrintNumber(number);
        return;
    }
    
    for (int i = 0; i < 10; ++i) {
        number[index + 1] = i + '0';
        Printf1ToMaxOfDigitsRecursively(number, length, index + 1);
    }
}

void Print1ToMaxOfNDigits(int n)
{
    if (n < 0) {
        return;
    }
    char *number = new char[n+1];
    memset(number, '0', n);
    number[n] = '\0';
    /* 第一种做法
    while (!Increment(number)) {
        PrintNumber(number);
    }
     */
    
    /* 第二种做法 */
    for (int i = 0; i < 10; ++i) {
        number[0] = i + '0';
        Printf1ToMaxOfDigitsRecursively(number, n, 0);
    }
    delete []number;
}

void RecorderOddEven(int *pData, unsigned int length)
{
    if (pData == NULL || length == 0) {
        return;
    }
    int *pBegin = pData;
    int *pEnd = pData + length - 1;
    while (pBegin < pEnd) {
        // 向后移动pBegin,直到它指向偶数
        while (pBegin < pEnd && (*pBegin & 0x1) != 0) {
            pBegin++;
        }
        // 向前移动pEnd,直到它指向奇数
        while (pBegin < pEnd && (*pEnd & 0x1) == 0) {
            pEnd--;
        }
        if (pBegin < pEnd) {
            int temp = *pBegin;
            *pEnd = temp;
            *pBegin = *pEnd;
        }
    }
    
//    Recorder(pData, length, isEven);
}

void Recorder(int *pData, unsigned int length, bool (*func)(int))
{
    if (pData == NULL || length == 0) {
        return;
    }
    int *pBegin = pData;
    int *pEnd = pData + length - 1;
    while (pBegin < pEnd) {
        // 向后移动pBegin,直到它指向偶数
        while (pBegin < pEnd && !func(*pBegin)) {
            pBegin++;
        }
        // 向前移动pEnd,直到它指向奇数
        while (pBegin < pEnd && func(*pEnd)) {
            pEnd--;
        }
        if (pBegin < pEnd) {
            int temp = *pBegin;
            *pEnd = temp;
            *pBegin = *pEnd;
        }
    }
}

bool isEven(int n)
{
    return (n & 0x1) == 0;
}

// 栈的压人、弹出序列
bool IsPopOrder(const int *pPush, const int *pPop, int nLength)
{
    bool bPossible = false;
    
    if (pPush != NULL && pPop != NULL && nLength > 0) {
        const int *pNextPush = pPush;
        const int *pNextPop = pPop;
        
        std::stack<int>stackData;
        while (pNextPop - pPop < nLength) {
            while (stackData.empty() || stackData.top() != *pNextPop) {
                if (pNextPush - pPush == nLength) {
                    break;
                }
                stackData.push(*pNextPush);
                pNextPush++;
            }
            
            if (stackData.top() != *pNextPop) {
                break;
            }
            
            stackData.pop();
            pNextPop++;
        }
        if (stackData.empty() && pNextPop - pPop == nLength) {
            bPossible = true;
        }
    }
    
    return bPossible;
}

// 从上往下打印二叉树

void PrintFromTopToBottom(BinaryTreeNode *pTreeRoot) // 不管是广度优先遍历一个有向图还是一棵树，都要用到队列。
{
    if (!pTreeRoot) {
        return;
    }
    std::deque<BinaryTreeNode *>dequeTreeNode;
    dequeTreeNode.push_back(pTreeRoot);
    while (dequeTreeNode.size()) {
        BinaryTreeNode *pNode = dequeTreeNode.front();
        dequeTreeNode.pop_front();
        printf("%d", pNode->m_nValue);
        
        if (pNode->m_pLeft) {
            dequeTreeNode.push_back(pNode->m_pLeft);
        }
        if (pNode->m_pRight) {
            dequeTreeNode.push_back(pNode->m_pRight);
        }
    }
    
}

// 二叉搜索树的后序遍历序列
bool VerifySquenceOfBST(int sequence[], int length)
{
    if (sequence == NULL || length <= 0) {
        return false;
    }
    
    int root = sequence[length - 1];
    // 在二叉搜索树中左子树的结点小于根结点
    int i = 0;
    for (; i < length; ++i) {
        if (sequence[i] > root) {
            break;
        }
    }
    
    // 在二叉搜索树种右子树的结点大于根结点
    int j = i;
    for (; j < length - 1; ++j) {
        if (sequence[j] < root) {
            return false;
        }
    }
    // 判断左子树是不是二叉搜索树
    bool left = true;
    if (i > 0) {
        left = VerifySquenceOfBST(sequence, i);
    }
    // 判断右子树是不是二叉搜索树
    bool right = true;
    if (i < length - 1) {
        right = VerifySquenceOfBST(sequence + i, length - i - 1);
    }
    return (left && right);
}

// 二叉树中和为某一值的路径
void FindPath(BinaryTreeNode *pRoot, int expectedSum, std::vector<int>& path, int& currentSum)
{
    currentSum += pRoot->m_nValue;
    path.push_back(pRoot->m_nValue);
    
    // 如果是叶结点，并且路径上结点的和等于输入的值
    // 打印出这条路径
    bool isLeaf = pRoot->m_pLeft == NULL && pRoot->m_pRight == NULL;
    if (currentSum == expectedSum && isLeaf) {
        printf("A path is found: ");
//        std::vector<int>::iterator iter = path.begin();
        auto iter = path.begin(); // 等同于上面
        for (; iter != path.end(); ++iter) {
            printf("%d\t", *iter);
        }
        printf("\n");
    }
    
    // 如果不是叶结点，则遍历它的结点
    if (pRoot->m_pLeft != NULL) {
        FindPath(pRoot->m_pLeft, expectedSum, path, currentSum);
    }
    if (pRoot->m_pRight != NULL) {
        FindPath(pRoot->m_pRight, expectedSum, path, currentSum);
    }
    
    // 在返回到父结点之前，在路径上删除呢当前结点，并在currentSum中减去当前结点的值
    currentSum -= pRoot->m_nValue;
    path.pop_back();
}

void FindPath(BinaryTreeNode *pRoot, int expectedSum)
{
    if (pRoot == NULL || expectedSum <= 0) {
        return;
    }
    std::vector<int>path;
    int currentSum = 0;
    FindPath(pRoot, expectedSum, path, currentSum);
}

// 复杂链表的复制
struct ComplexListNode
{
    int             m_nValue;
    ComplexListNode *m_pNext;
    ComplexListNode *m_pSibling;
};

void CloneNodes(ComplexListNode *pHead) // 复制原始链表的任意结点N并创建新结点N‘，再把N’链接到N的后面。
{
    ComplexListNode *pNode = pHead;
    while (pNode != NULL) {
        ComplexListNode *pCloned = new ComplexListNode();
        pCloned->m_nValue = pNode->m_nValue;
        pCloned->m_pNext = pNode->m_pNext;
        pCloned->m_pSibling = NULL;
        
        pNode->m_pNext = pCloned;
        pNode = pCloned->m_pNext;
    }
}

void ConnectSiblingNodes(ComplexListNode *pHead) // 如果原始链表上的结点N的m_pSibling指向S，则它对应的复制结点N‘的m_pSibling指向S的下一结点S’。
{
    ComplexListNode *pNode = pHead;
    while (pNode != NULL) {
        ComplexListNode *pCloned = pNode->m_pNext;
        if (pNode->m_pSibling != NULL) {
            pCloned->m_pSibling = pNode->m_pSibling->m_pNext;
        }
        pNode = pCloned->m_pNext;
    }
}

ComplexListNode *ReconnectNodes(ComplexListNode *pHead) // 把第二步得到的链表拆分成两个链表，奇数位置上的结点组成原始链表，偶数位置上的结点组成复制出来的链表。
{
    ComplexListNode *pNode = pHead;
    ComplexListNode *pClonedHead = NULL;
    ComplexListNode *pClonedNode = NULL;
    if (pNode != NULL) {
        pClonedHead = pClonedNode = pNode->m_pNext;
        pNode->m_pNext = pClonedNode->m_pNext;
        pNode = pNode->m_pNext;
    }
    
    while (pNode != NULL) {
        pClonedNode->m_pNext = pNode->m_pNext;
        pClonedNode = pClonedNode->m_pNext;
        pNode->m_pNext = pClonedNode->m_pNext;
        pNode = pNode->m_pNext;
    }
    return pClonedNode;
}

ComplexListNode *Clone(ComplexListNode *pHead)
{
    CloneNodes(pHead);
    ConnectSiblingNodes(pHead);
    return ReconnectNodes(pHead);
}

bool g_bInputInvalid = false;
bool CheckInvalidArray(int *numbers, int length)
{
    g_InvalidInput = false;
    if (numbers == NULL && length <= 0) {
        g_InvalidInput = true;
    }
    return g_InvalidInput;
}

bool CheckMoreThanHalf(int *numbers, int length, int number)
{
    int times = 0;
    for (int i = 0; i < length; i++) {
        if (numbers[i] == number) {
            times++;
        }
    }
    
    bool isMoreThanHalf = true;
    if (times * 2 <= length) {
        g_InvalidInput = true;
        isMoreThanHalf = false;
    }
    
    return isMoreThanHalf;
}

int MoreThanHalfNum(int *numbers, int length)
{
    if (CheckInvalidArray(numbers, length)) {
        return 0;
    }
    
    int middle = length >> 1;
    int start = 0;
    int end = length - 1;
    int index = Partition(numbers, length, start, end);
    while (index != middle) {
        if (index > middle) {
            end = index - 1;
            index = Partition(numbers, length, start, end);
        }
        else {
            start = index + 1;
            index = Partition(numbers, length, start, end);
        }
    }
    
    int result = numbers[middle];
    if (!CheckMoreThanHalf(numbers, length, result)) {
        result = 0;
    }
    return result;
}

typedef multiset<int, greater<int> > intSet;
typedef multiset<int, greater<int> >::iterator setIterator;
void GetLeastNumbers(const vector<int>& data, intSet& leastNumbers, int k)
{
    leastNumbers.clear();
    if (k < 1 || data.size() < k) {
        return;
    }
    
    vector<int>::const_iterator iter = data.begin();
    for (; iter != data.end(); ++iter) {
        if ((leastNumbers.size()) < k) {
            leastNumbers.insert(*iter);
        } else {
            setIterator iterGreatest = leastNumbers.begin();
            if (*iter < *(leastNumbers.begin())) {
                leastNumbers.erase(iterGreatest);
                leastNumbers.insert(*iter);
            }
        }
    }
}

int FindGreatestSumOfSubArray(int *pData, int nLength)
{
    if (pData == NULL || (nLength <= 0)) {
        g_InvalidInput = true;
        return 0;
    }
    g_InvalidInput = false;
    
    int nCurSum = 0;
    int nGreatestSum = 0x80000000;
    for (int i = 0; i < nLength; ++i) {
        if (nCurSum <= 0) {
            nCurSum = pData[i];
        }
        else {
            nCurSum += pData[i];
        }
        if (nCurSum > nGreatestSum) {
            nGreatestSum = nCurSum;
        }
    }
    return nGreatestSum;
}

// 动态规划


void reverse_c(char arr[], int start, int end)
{
    int mid = (start + end) / 2;
    for (int s = start, i = 1; i < mid; s++, i++) {
        char temp = arr[s];
        arr[s] = arr[end - i];
        arr[end - 1] = temp;
    }
}

void useReverse_c(char arr[], int len, int m)
{
    reverse_c(arr, 0, m);
    reverse_c(arr, m, len);
    reverse_c(arr, 0, len);
}

class AA
{
private:
    int n1;
    int n2;
public:
    AA():n2(0), n1(n2 + 2)
    {
        
    }
    
    void Print()
    {
        std::cout << "n1: " << n1 << ", n2: " << n2 << std::endl;
    }
};

// addition是指针函数，一个返回类型是指针的函数
int* additon(int a, int b) {
    int* sum = new int(a + b);
    return sum;
}

int subtraction(int a, int b) {
    return a - b;
}

int operation(int x, int y, int (*func)(int, int)) {
    return (*func)(x, y);
}

// minus是函数指针，指向函数的指针
int (*minus2)(int, int) = subtraction;

vector<int> twoSum(vector<int>& numbers, int target) {
    int l = 0, r = numbers.size() - 1, sum;
    while (l < r) {
        sum = numbers[l] + numbers[r];
        if (sum == target) {
            break;
        }
        if (sum < target) {
            ++l;
        } else {
            --r;
        }
    }
//    return vector<int>{l + 1, r + 1};
    return vector<int>{numbers[l], numbers[r]};
}

void mergeArray(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int pos = m-- + n-- - 1;
    while (m >= 0 && n >= 0) {
        nums1[pos--] = nums1[m] > nums2[n] ? nums1[m--] : nums2[n--];
    }
    while (n >= 0) {
        nums1[pos--] = nums2[n--];
    }
}

// 合并两个排序的链表
ListNode* Merge(ListNode* pHead1, ListNode* pHead2) {
    if (pHead1 == NULL) {
        return pHead2;
    } else if (pHead2 == NULL) {
        return pHead1;
    }
    
    ListNode* pMergedHead = NULL;
    if (pHead1->m_nValue < pHead2->m_nValue) {
        pMergedHead = pHead1;
        pMergedHead->m_pNext = Merge(pHead1->m_pNext, pHead2);
    } else {
        pMergedHead = pHead2;
        pMergedHead->m_pNext = Merge(pHead1, pHead2->m_pNext);
    }
    return pMergedHead;
}

// 快慢指针
struct ListNodeP {
    int val;
    ListNodeP *next;
    ListNodeP(int x) : val(x), next(nullptr) {}
};

ListNodeP *detectCycle(ListNodeP *head) {
    ListNodeP *slow = head, *fast = head;
    // 判断是否存在环路
    do {
        if (!fast || !fast->next) {
            return nullptr;
        }
        fast = fast->next->next;
        slow = slow->next;
    } while(fast != slow);
    // 如果存在，查找环路节点
    fast = head;
    while (fast != slow) {
        slow = slow->next;
        fast = fast->next;
    }
    return fast;
}

string minWindow(string S, string T) {
    vector<int> chars(128, 0);
    vector<bool> flag(128, false);
    // 先统计T中的字符情况
    for (int i = 0; i < T.size(); ++i) {
        flag[T[i]] = true;
        ++chars[T[i]];
    }
    // 移动滑动窗口，不断更改统计数据
    int cnt = 0, l = 0, min_l = 0, min_size = S.size() + 1;
    for (int r = 0; r < S.size(); ++r) {
        if (flag[S[r]]) {
            if (--chars[S[r]] >= 0) {
                ++cnt;
            }
            // 若目前滑动窗口已包含T中全部字符，
            // 则尝试将l右移，在不影响结果的情况下获得最短子字符串
            while (cnt == T.size()) {
                if (r - l + 1 < min_size) {
                    min_l = l;
                    min_size = r - l + 1;
                }
                if (flag[S[l]] && ++chars[S[l]] > 0) {
                    --cnt;
                }
                ++l;
            }
        }
    }
    return min_size > S.size() ? "" : S.substr(min_l, min_size);
}

int mySqrt2(int a) {
   long x = a;
   while (x * x > a) {
      x = (x + a / x) / 2;
    }
    return x;
}

int mySqrt(int a) {
    if (a == 0) {
        return a;
    }
    int l = 1, r = a, mid, sqrt;
    while (l <= r) {
        mid = l + (r - l) / 2;
        sqrt = a / mid;
        if (sqrt == mid) {
            return mid;
        } else if (mid > sqrt) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return r;
}

// 辅函数
int lower_bound(vector<int> &nums, int target) {
    int l = 0, r = nums.size(), mid;
    while (l < r) {
        mid = (l + r) / 2;
        if (nums[mid] >= target) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
}

// 辅函数
int upper_bound(vector<int> &nums, int target) {
    int l = 0, r = nums.size(), mid;
    while (l < r) {
        mid = (l + r) / 2;
        if (nums[mid] > target) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
}

// 主函数
vector<int> searchRange(vector<int>& nums, int target) {
    if (nums.empty()) {
        return vector<int>{-1, -1};
    }
    int lower = lower_bound(nums, target);
    int upper = upper_bound(nums, target) - 1;// 这里需要减1位
    if (lower == nums.size() || nums[lower] != target) {
        return vector<int>{-1, -1};
    }
    return vector<int>{lower, upper};
}

bool search(vector<int>& nums, int target) {
    int start = 0, end = nums.size() - 1;
    while (start <= end) {
        int mid = (start + end) / 2;
        if (nums[mid] == target) {
            return true;
        }
        if (nums[start] == nums[mid]) {
            // 无法判断哪个区间是增序的
            ++start;
        } else if (nums[mid] <= nums[end]) {
            // 右区间是增序的
            if (target > nums[mid] && target <= nums[end]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        } else {
            // 左区间是增序的
            if (target >= nums[start] && target < nums[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
    }
    return false;
}

int _climbStairs(int n) {
    if (n < 2) {
        return n;
    }
    vector<int> dp(n + 1, 1);
    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}

// 给定 n 节台阶，每次可以走一步或走两步，求一共有多少种方式可以走完这些台阶。
int climbStairs(int n) {
    if (n <= 2) {
        return n;
    }
    int pre2 = 1, pre1 = 2, cur = 0;
    for (int i = 2; i < n; ++i) {
        cur = pre1 + pre2;
        pre2 = pre1;
        pre1 = cur;
    }
    return cur;
}

//输入是一个一维数组，表示每个房子的钱财数量;输出是劫匪可以最多抢劫的钱财数量。
//Input: [2,7,9,3,1]
//Output: 12

//定义一个数组 dp，dp[i] 表示抢劫到第 i 个房子时，可以抢劫的最大数量。我们考虑 dp[i]， 此时可以抢劫的最大数量有两种可能，一种是我们选择不抢劫这个房子，此时累计的金额即为 dp[i-1];另一种是我们选择抢劫这个房子，那么此前累计的最大金额只能是 dp[i-2]，因为我们不 能够抢劫第 i-1 个房子，否则会触发警报机关。因此本题的状态转移方程为 dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])。

int _rob(vector<int> & nums) {
    if (nums.empty()) {
        return 0;
    }
    size_t n = nums.size();
    vector<int> dp(n + 1, 0);
    dp[1] = nums[0];
    for (int i = 2; i <= n; ++i) {
        dp[i] = max(dp[i-1], nums[i-1] + dp[i-2]);
    }
    return dp[n];
}
   
int rob(vector<int> & nums) {
    if (nums.empty()) {
        return 0;
    }
    size_t n = nums.size();
    if (n == 1) {
        return nums[0];
    }
    int pre2 = 0, pre1 = 0, cur = 0;
    for (int i = 0; i < n; ++i) {
        cur = max(pre2 + nums[i], pre1);
        pre2 = pre1;
        pre1 = cur;
    }
    return cur;
}

//int numberOfAritheticSlices(vector<int>& nums) {
//    int n = nums.size();
//    if (n < 3) {
//        return 0;
//    }
//    vector<int> dp(n, 0);
//    for (int i = 2; i < n; ++i) {
//        if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
//            dp[i] = dp[i-1] + 1;
//        }
//    }
//    return accumlate(dp.begin(), dp.end(), 0);
//}

//题目描述
//给定一个 m × n 大小的非负整数矩阵，求从左上角开始到右下角结束的、经过的数字的和最 小的路径。每次只能向右或者向下移动。
//输入输出样例
//  输入是一个二维数组，输出是最优路径的数字和。
//Input:
//[[1,3,1],
//[1,5,1],
// [4,2,1]]
//Output: 7
//在这个样例中，最短路径为 1->3->1->1->1。 题解
//我们可以定义一个同样是二维的 dp 数组，其中 dp[i][j] 表示从左上角开始到 (i, j) 位置的最 优路径的数字和。因为每次只能向下或者向右移动，我们可以很容易得到状态转移方程 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]，其中 grid 表示原数组。
int _minPathSum(vector<vector<int>>& grid) {
    size_t m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) {
                dp[i][j] = grid[i][j];
            } else if (i == 0) {
                dp[i][j] = dp[i][j-1] + grid[i][j];
            } else if (j == 0) {
                dp[i][j] = dp[i-1][j] + grid[i][j];
            } else {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
    }
    return dp[m-1][n-1];
}

int minPathSum(vector<vector<int>>& grid) {
    size_t m = grid.size(), n = grid[0].size();
    vector<int> dp(n, 0);
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) {
                dp[j] = grid[i][j];
            } else if (i == 0) {
                dp[j] = dp[j - 1] + grid[i][j];
            } else if (j == 0) {
                dp[j] = dp[j] + grid[i][j];
            } else {
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j];
            }
        }
    }
    return dp[n-1];
}

vector<vector<int>> updateMartix(vector<vector<int>>& matrix) {
    if (matrix.empty()) {
        return {};
    }
    int n = matrix.size(), m = matrix[0].size();
    vector<vector<int>> dp(n, vector<int>(m, INT_MAX - 1));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; ++j) {
            if (matrix[i][j] == 0) {
                dp[i][j] = 0;
            } else {
                if (j > 0) {
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1);
                }
                if (i > 0) {
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1);
                }
            }
        }
    }
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            if (matrix[i][j] != 0) {
                if (j < m - 1) {
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1);
                }
                if (i < n - 1) {
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1);
                }
            }
        }
    }
    return dp;
}

int maximalSquare(vector<vector<char>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) {
        return 0;
    }
    int m = matrix.size(), n = matrix[0].size(), max_side = 0;
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (matrix[i-1][j-1] == '1') {
                dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1;
            }
            max_side = max(max_side, dp[i][j]);
        }
    }
    return max_side * max_side;
}

//题目描述
//  给定一个正整数，求其最少可以由几个完全平方数相加构成。
//输入输出样例
//– 47/143 –
//  输入是给定的正整数，输出也是一个正整数，表示输入的数字最少可以由几个完全平方数相 加构成。
//Input: n = 13
//Output: 2
//在这个样例中，13 的最少构成方法为 4+9。 题解
//对于分割类型题，动态规划的状态转移方程通常并不依赖相邻的位置，而是依赖于满足分割 条件的位置。我们定义一个一维矩阵 dp，其中 dp[i] 表示数字 i 最少可以由几个完全平方数相加 构成。在本题中，位置 i 只依赖 i - k2 的位置，如 i - 1、i - 4、i - 9 等等，才能满足完全平方分割 的条件。因此 dp[i] 可以取的最小值即为 1 + min(dp[i-1], dp[i-4], dp[i-9] · · · )。

int numSquares(int n) {
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j * j <= i; ++j) {
            dp[i] = min(dp[i], dp[i-j*j] + 1);
        }
    }
    return dp[n];
}

int numDecodings(string s) {//"226"  BZ(2 26)、VF(22 6) 或 BBF(2 2 6)
    int n = s.length();
    if (n == 0) {
        return 0;
    }
    int prev = s[0] - '0';
    if (!prev) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    vector<int> dp(n + 1, 1);
    for (int i = 2; i <= n; ++i) {
        int cur = s[i-1] - '0';
        if ((prev == 0 || prev > 2) && cur == 0) {
            return 0;
        }
        if ((prev < 2 && prev > 0) || (prev == 2 && cur < 7)) {
            if (cur) {
                dp[i] = dp[i-2] + dp[i-1];
            } else {
                dp[i] = dp[i-2];
            }
        } else {
            dp[i] = dp[i-1];
        }
        prev = cur;
    }
    return dp[n];
}

//Input: s = "applepenapple", wordDict = ["apple", "pen"]
//Output: true
//在这个样例中，字符串可以被分割为 [“apple”,“pen”,“apple”]。
bool wordBreak(string s, vector<string>& wordDict) {
    int n = s.length();
    if (n <= 0) {
        return false;
    }
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; ++i) {
        for (const string & word: wordDict) {
            int len = word.length();
            if (i >= len && s.substr(i - len, len) == word) {
                dp[i] = dp[i] || dp[i - len];
            }
        }
    }
    return dp[n];
}

//输入是一个一维数组，输出是一个正整数，表示最长递增子序列的长度。
//   Input: [10,9,2,5,3,7,101,18]
//   Output: 4
//在这个样例中，最长递增子序列之一是 [2,3,7,18]。
int _lengthOfLIS(vector<int>& nums) {
    int max_length = 0, n = nums.size();
    if (n <= 1) {
        return n;
    }
    vector<int> dp(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        max_length = max(max_length, dp[i]);
    }
    return max_length;
}

int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    if (n <= 1) {
        return n;
    }
    vector<int> dp;
    dp.push_back(nums[0]);
    for (int i = 1; i < n; ++i) {
        if (dp.back() < nums[i]) {
            dp.push_back(nums[i]);
        } else {
            auto itr = lower_bound(dp.begin(), dp.end(), nums[i]);
            *itr = nums[i];
        }
    }
    return dp.size();
}

//输入是两个字符串，输出是一个整数，表示它们满足题目条件的长度。
//Input: text1 = "abcde", text2 = "ace"
//Output: 3
//在这个样例中，最长公共子序列是“ace”。
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length(), n = text2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (text1[i-1] == text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}

//我们可以用动态规划来解决背包问题。以 0-1 背包问题为例。我们可以定义一个二维数组 dp 存储最大价值，其中 dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到的最大价值。在我们遍 历到第 i 件物品时，在当前背包总容量为 j 的情况下，如果我们不将物品 i 放入背包，那么 dp[i][j] = dp[i-1][j]，即前 i 个物品的最大价值等于只取前 i-1 个物品时的最大价值;如果我们将物品 i 放 入背包，假设第 i 件物品体积为 w，价值为 v，那么我们得到 dp[i][j] = dp[i-1][j-w] + v。我们只需 在遍历过程中对这两种情况取最大值即可，总时间复杂度和空间复杂度都为 O(NW)。
int _knapsack(vector<int> weights, vector<int> values, int N, int W) {
    vector<vector<int>> dp(N + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= N; ++i) {
        int w = weights[i-1], v = values[i-1];
        for (int j = 1; j <= W; ++j) {
            if (j >= w) {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v);
            } else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    return dp[N][W];
}

int knapsack(vector<int> weights, vector<int> values, int N, int W) {
    vector<int> dp(W + 1, 0);
    for (int i = 1; i <= N; ++i) {
        int w = weights[i-1], v = values[i-1];
        for (int j = W; j >= w; --j) {
            dp[j] = max(dp[j], dp[j-w] + v);
        }
    }
    return dp[W];
}

int knapsack_(vector<int> weights, vector<int> values, int N, int W) {
    vector<int> dp(W + 1, 0);
    for (int i = 1; i <= N; ++i) {
       int w = weights[i-1], v = values[i-1];
       for (int j = w; j <= W; ++j) {
          dp[j] = max(dp[j], dp[j-w] + v);
       }
    }
    return dp[W];
}

// 输入是一个一维正整数数组，输出时一个布尔值，表示是否可以满足题目要求。
//Input: [1,5,11,5]
//Output: true
//在这个样例中，满足条件的分割方法是 [1,5,5] 和 [11]。
bool _canPartition(vector<int> &nums) {
//    int sum = accumulate(nums.begin(), nums.end(), 0);
    int sum = 0;
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++) {
        sum += *it;
    }
    if (sum % 2) {
        return false;
    }
    int target = sum / 2, n = nums.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));
    for (int i = 0; i <= n; ++i) {
        dp[i][0] = true;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = nums[i-1]; j <= target; ++j) {
            dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i-1]];
        }
    }
    return dp[n][target];
}

bool canPartition(vector<int> &nums) {
//    int sum = accumulate(nums.begin(), nums.end(), 0);
    int sum = 0;
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++) {
        sum += *it;
    }
    if (sum % 2) {
        return false;
    }
    int target = sum / 2, n = nums.size();
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; ++i) {
        for (int j = target; j >= nums[i-1]; --j) {
            dp[j] = dp[j] || dp[j-nums[i-1]];
        }
    }
    return dp[target];
}

// 辅函数
pair<int, int> count(const string & s) {
    int count0 = s.length(), count1 = 0;
    for (const char & c: s) {
        if (c == '1') {
            ++count1;
            --count0;
        }
    }
    return make_pair(count0, count1);
}

// 主函数
int findMaxForm(vector<string>& strs, int m, int n) {
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (const string & str: strs) {
        auto [count0, count1] = count(str);
        for (int i = m; i >= count0; --i) {
            for (int j = n; j >= count1; --j) {
                dp[i][j] = max(dp[i][j], 1 + dp[i-count0][j-count1]);
            }
        }
    }
    return dp[m][n];
}

int coinChange(vector<int>& coins, int amount) {
    if (coins.empty()) {
        return -1;
    }
    vector<int> dp(amount + 1, amount + 2);
    dp[0] = 0;
    for (int i = 1; i <= amount; ++i) {
        for (const int & coin: coins) {
            if (i >= coin) {
                dp[i] = min(dp[i], dp[i-coin] + 1);
            }
        }
    }
    return dp[amount] == amount + 2 ? - 1 : dp[amount];
}

int minDistance(string word1, string word2) {
    int m = word1.length(), n = word2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i <= m; ++i) {
        for (int j = 0; j <= n; ++j) {
            if (i == 0) {
                dp[i][j] = j;
            } else if (j == 0) {
                dp[i][j] = i;
            } else {
                dp[i][j] = min(dp[i-1][j-1] + ((word1[i-1] == word2[j-1]) ? 0 : 1), min(dp[i-1][j] + 1, dp[i][j-1] + 1));
            }
        }
    }
    return dp[m][n];
}

//输入一个一维整数数组，表示每天的股票价格;输出一个整数，表示最大的收益。
//
//7.8 股票交易 – 60/143 – Input: [7,1,5,3,6,4]
//Output: 5
//在这个样例中，最大的利润为在第二天价格为 1 时买入，在第五天价格为 6 时卖出。
int maxProfit(vector<int>& prices) {
    int sell = 0, buy = INT_MIN;
    for (int i = 0; i < prices.size(); ++i) {
        buy = max(buy, -prices[i]);
        sell = max(sell, buy + prices[i]);
    }
    return sell;
}

//输入一个一维整数数组，表示每天的股票价格;以及一个整数，表示可以买卖的次数 k。输 出一个整数，表示最大的收益。
//Input: [3,2,6,5,0,3], k = 2
//Output: 7
//在这个样例中，最大的利润为在第二天价格为 2 时买入，在第三天价格为 6 时卖出;再在第 五天价格为 0 时买入，在第六天价格为 3 时卖出。
int maxProfitUnlimited(vector<int> prices) {
    int maxProfit = 0;
    for (int i = 1; i < prices.size(); ++i) {
        if (prices[i] > prices[i-1]) {
            maxProfit += prices[i] - prices[i-1];
        }
    }
    return maxProfit;
}

int maxiumProfit(int k, vector<int>& prices) {
    int days = prices.size();
    if (days < 2) {
        return 0;
    }
    if (k >= days) {
        return maxProfitUnlimited(prices);
    }
    vector<int> buy(k + 1, INT_MIN), sell(k + 1, 0);
    for (int i = 0; i < days; ++i) {
        for (int j = 1; j <= k; ++j) {
            buy[j] = max(buy[j], sell[j-1] - prices[i]);
            sell[j] = max(sell[j], buy[j] + prices[i]);
        }
    }
    return sell[k];
}

ListNode* ReverseListNew(ListNode* pHead) {
    ListNode *pNode = pHead;
    ListNode *pPrev = NULL;
    while (pNode != NULL) {
        ListNode *pNext = pNode->m_pNext;
        pNode->m_pNext = pPrev;
        
        pPrev = pNode;
        pNode = pNext;
    }
    return pPrev;
}

ListNode *reverseList_DiguiNew(ListNode* pHead, ListNode* pHead2 = NULL) {
    if (pHead == NULL) {
        return pHead2;
    }
    ListNode *pNext = pHead->m_pNext;
    pHead->m_pNext = pHead2;
    return reverseList_DiguiNew(pNext, pHead);
}

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (!l2) {
        return l1;
    }
    if (!l1) {
        return l2;
    }
    if (l1->m_nValue > l2->m_nValue) {
        l2->m_pNext = mergeTwoLists(l1, l2->m_pNext);
        return l2;
    }
    l1->m_pNext = mergeTwoLists(l1->m_pNext, l2);
    return l1;
}

ListNode* mergeTwoListsNew(ListNode *l1, ListNode *l2) {
    ListNode *dummy = new ListNode(), *node = dummy;
    while (l1 && l2) {
        if (l1->m_nValue <= l2->m_nValue) {
            node->m_pNext = l1;
            l1 = l1->m_pNext;
        } else {
            node->m_pNext = l2;
            l2 = l2->m_pNext;
        }
        node = node->m_pNext;
    }
    node->m_pNext = l1? l1 : l2;
    return dummy->m_pNext;
}

// 快排
void quick_sort(vector<int>& nums, int l, int r) {
    if (l + 1 >= r) {
        return;
    }
    int first = 1, last = r - 1, key = nums[first];
    while (first < last) {
        while (first < last && nums[last] >= key) {
            --last;
        }
        nums[first] = nums[last];
        while (first < last && nums[first] <= key) {
            ++first;
        }
        nums[last] = nums[first];
    }
    nums[first] = key;
    quick_sort(nums, l, first);
    quick_sort(nums, first + 1, r);
}

void merge_sort(vector<int>& nums, int l, int r, vector<int>& temp) {
    if (l + 1 >= r) {
        return;
    }
    // divide
    int m = l + (r - 1) / 2;
    merge_sort(nums, l, m, temp);
    merge_sort(nums, m, r, temp);
    // conquer
    int p = l, q = m, i = l;
    while (p < m || q < r) {
        if (q >= r || (p < m && nums[p] <= nums[q])) {
            temp[i++] = nums[p++];
        } else {
            temp[i++] = nums[q++];
        }
    }
    for (i = l; i < r; ++i) {
        nums[i] = temp[i];
    }
}

void GetMemory(char *p)
{
    p = (char *)malloc(100);
}

char *GetMemory2(void)
{
    char p[] = "hello world";
    return p;
}

void Test(void)
{
    char *str = NULL;
    GetMemory(str);
    strcpy(str, "hello world");
    printf(str);
    // 程序崩溃。
    // 因为 GetMemory 并不能传递动态内存， Test 函数中的 str 一直都是 NULL。 strcpy(str, "hello world");将使程序崩 溃。
}

void Test2(void)
{
    char *str = NULL;
    str = GetMemory2();
    printf(str);
    // 可能是乱码。
    // 因为 GetMemory 返回的是指向“栈内存” 的指针，该指针的地址不是 NULL，但其原 现的内容已经被清除，新内容不可知。
}

void GetMemory2(char **p, int num) {
    *p = (char *)malloc(num);
}

void _Test(void) {
    char *str = NULL;
    GetMemory2(&str, 100);
    strcpy(str, "hello");
    printf(str);
//    free(str);
//    str = NULL;
    // (1)能够输出 hello
    // (2)内存泄漏
}

void Test_(void) {
    char *str = (char *) malloc(100);
    strcpy(str, "hello");
    free(str);
//    str = NULL;
    if (str != NULL) {
        strcpy(str, "world");
        printf(str);
    }
//    篡改动态内存区的内容，后果难以预 料，非常危险。
//    因为 free(str);之后，str 成为野指针， if(str != NULL)语句不起作用。
}

char *_strcpy(char *strDest, const char *strSrc)
{
    assert((strDest != NULL) && (strSrc != NULL));
    char *address = strDest;
    while ((*strDest++ = *strSrc++) != '\0');
    return address;
    // strcpy 能把 strSrc 的内容复制到 strDest，为什么还要 char * 类型的返回值? 答:为了实现链式表达式。
    // 例如 int length = strlen( strcpy( strDest, “hello world”) );
}

// 插入排序
void insertion_sort(vector<int>& nums, int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = i; j > 0 && nums[j] < nums[j-1]; --j) {
            swap(nums[j], nums[j-1]);
        }
    }
}

// 冒泡排序
void bubble_sort(vector<int>& nums, int n) {
    bool swapped;
    for (int i = 1; i < n; ++i) {
        swapped = false;
        for (int j = 1; j < n - i + 1; ++j) {
            if (nums[j] < nums[j-1]) {
                swap(nums[j], nums[j-1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
}

// 选择排序
void selection_sort(vector<int>& nums, int n) {
    int mid;
    for (int i = 0; i < n - 1; ++i) {
        mid = i;
        for (int j = i + 1; j < n; ++j) {
            if (nums[j] < nums[mid]) {
                mid = j;
            }
        }
        swap(nums[mid], nums[i]);
    }
}

void sort() {
    vector<int> nums = {1,3,5,7,2,6,4,8,9,2,8,7,6,0,3,5,9,4,1,0};
    vector<int> temp(nums.size());
//    sort(nums.begin(), nums.end());
//    quick_sort(nums, 0, nums.size());
//    merge_sort(nums, 0, nums.size(), temp);
    insertion_sort(nums, nums.size());
    bubble_sort(nums, nums.size());
    selection_sort(nums, nums.size());
}

// 快速选择
int quickSelection(vector<int>& nums, int l, int r) {
    int i = l + 1, j = r;
    while (true) {
        while (i < r && nums[i] <= nums[l]) {
            ++i;
        }
        while (l < j && nums[j] >= nums[l]) {
            --j;
        }
        if (i >= j) {
            break;
        }
        swap(nums[i], nums[j]);
    }
    swap(nums[l], nums[j]);
    return j;
}

int findKthLargetst(vector<int>& nums, int k) {
    int l = 0, r = nums.size() - 1, target = nums.size() - k;
    while (l < r) {
        int mid = quickSelection(nums, l, r);
        if (mid == target) {
            return nums[mid];
        }
        if (mid < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return nums[l];
}

// 桶排序
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> counts;
    int max_count = 0;
    for (const int & num : nums) {
        max_count = max(max_count, ++counts[num]);
    }
    
    vector<vector<int>> buckets(max_count + 1);
    for (const auto & p : counts) {
        buckets[p.second].push_back(p.first);
    }
    
    vector<int> ans;
    for (int i = max_count; i >= 0 && ans.size() < k; --i) {
        for (const int & num : buckets[i]) {
            ans.push_back(num);
            if (ans.size() == k) {
                break;
            }
        }
    }
    return ans;
}

vector<int> direction{-1, 0, 1, 0, -1};

int _maxAreaOfIsland(vector<vector<int>>& grid) {
    int m = grid.size(), n = m ? grid[0].size() : 0, local_area, area = 0, x, y;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j]) {
                local_area = 1;
                grid[i][j] = 0;
                stack<pair<int, int>> island;
                island.push({i, j});
                while (!island.empty()) {
                    auto [r, c] = island.top();
                    island.pop();
                    for (int k = 0; k < 4; ++k) {
                        x = r + direction[k], y = direction[k+1];
                        if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                            grid[x][y] = 0;
                            ++local_area;
                            island.push({x, y});
                        }
                    }
                }
                area = max(area, local_area);
            }
        }
    }
    return area;
}

// 辅函数
int dfs(vector<vector<int>>& grid, int r, int c) {
    if (grid[r][c] == 0) {
        return 0;
    }
    grid[r][c] = 0;
    int x, y, area = 1;
    for (int i = 0; i < 4; ++i) {
        x = r + direction[i], y = c + direction[i+1];
        if (x >= 0 && x < grid.size() && y >= 0 && y < grid[0].size()) {
            area += dfs(grid, x, y);
        }
    }
    return area;
}

int maxAreaOfIsland(vector<vector<int>>& grid) {
    if (grid.empty() || grid[0].empty()) {
        return 0;
    }
    int max_area = 0;
    for (int i = 0; i < grid.size(); ++i) {
        for (int j = 0; j < grid[0].size(); ++j) {
            if (grid[i][j] == 1) {
                max_area = max(max_area, dfs(grid, i, j));
            }
        }
    }
    return max_area;
}

// 辅函数
int _dfs(vector<vector<int>>& grid, int r, int c) {
    if (r < 0 || r >= grid.size() ||
       c < 0 || c >= grid[0].size() || grid[r][c] == 0) {
       return 0;
    }
    grid[r][c] = 0;
    return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) +
              dfs(grid, r, c + 1) + dfs(grid, r, c - 1);
}

// 主函数
int maxAreaOfIsland_(vector<vector<int>>& grid) {
    if (grid.empty() || grid[0].empty()) return 0;
    int max_area = 0;
    for (int i = 0; i < grid.size(); ++i) {
       for (int j = 0; j < grid[0].size(); ++j) {
           max_area = max(max_area, _dfs(grid, i, j));
       }
    }
    return max_area;
}

// 输入是一个二维数组，输出是一个整数，表示朋友圈数量。因为朋友关系具有对称性，该二 维数组为对称矩阵。同时，因为自己是自己的朋友，对角线上的值全部为 1。
//Input:
//[[1,1,0],
//[1,1,0],
// [0,0,1]]
//Output: 2
//在这个样例中，[1,2] 处于一个朋友圈，[3] 处于一个朋友圈。

//输入是一个一维整数数组，输出是一个二维数组，表示输入数组的所有排列方式。
//Input: [1,2,3]
//Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
//  可以以任意顺序输出，只要包含了所有排列方式即可。
void backtracking(vector<int>& nums, int level, vector<vector<int>>& ans) {
    if (level == nums.size() - 1) {
        ans.push_back(nums);
        return;
    }
    for (int i = level; i < nums.size(); i++) {
        swap(nums[i], nums[level]); // 修改当前节点状态
        backtracking(nums, level+1, ans); // 递归子节点
        swap(nums[i], nums[level]); // 回改当前节点状态
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> ans;
    backtracking(nums, 0, ans);
    return ans;
}

//给定一个整数 n 和一个整数 k，求在 1 到 n 中选取 k 个数字的所有组合方法。
//
//6.3 回溯法 输入输出样例
//输入是两个正整数 n 和 k，输出是一个二维数组，表示所有组合方式。 Input: n = 4, k = 2
//Output: [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
void backtracking(vector<vector<int>>& ans, vector<int>& comb, int& count, int pos, int n, int k) {
    if (count == k) {
        ans.push_back(comb);
        return;
    }
    for (int i = pos; i <= n; ++i) {
        comb[count++] = i; // 修改当前节点状态
        backtracking(ans, comb, count, i + 1, n, k); // 递归子节点
        --count; // 回改当前节点状态
    }
}

vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> ans;
    vector<int> comb(k, 0);
    int count = 0;
    backtracking(ans, comb, count, 1, n, k);
    return ans;
}

//输入是一个二维字符数组和一个字符串，输出是一个布尔值，表示字符串是否可以被寻找 到。
//Input: word = "ABCCED", board =
//[[’A’,’B’,’C’,’E’],
// [’S’,’F’,’C’,’S’],
// [’A’,’D’,’E’,’E’]]
//Output: true
//从左上角的’A’ 开始，我们可以先向右、再向下、最后向左，找到连续的"ABCCED"。
void backtracking(int i, int j, vector<vector<char>>& board, string& word, bool
                  & find, vector<vector<bool>>& visited, int pos) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size()) {
        return;
    }
    if (visited[i][j] || find || board[i][j] != word[pos]) {
        return;
    }
    if (pos == word.size() - 1) {
        find = true;
        return;
    }
    visited[i][j] = true; // 修改当前节点状态
    // 递归子节点
    backtracking(i + 1, j, board, word, find, visited, pos + 1);
    backtracking(i - 1, j, board, word, find, visited, pos + 1);
    backtracking(i, j + 1, board, word, find, visited, pos + 1);
    backtracking(i, j - 1, board, word, find, visited, pos + 1);
    visited[i][j] = false; // 回改当前节点状态
}

bool exist(vector<vector<char>>& board, string word) {
    if (board.empty()) return false;
    int m = board.size(), n = board[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    bool find = false;
    for (int i = 0; i < m; ++i) {
       for (int j = 0; j < n; ++j) {
           backtracking(i, j, board, word, find, visited, 0);
       }
    }
    return find;
}

// 输入是一个整数 n，输出是一个二维字符串数组，表示所有的棋盘表示方法。
//Input: 4
//Output: [
// [".Q..", // Solution 1
//  "...Q",
//  "Q...",
//  "..Q."],
// ["..Q.", // Solution 2
//  "Q...",
//  "...Q",
//  ".Q.."]
//]
//在这个样例中，点代表空白位置，Q 代表皇后。
void backtracking(vector<vector<string>>& ans, vector<string>& board, vector<bool>& column, vector<bool>& ldiag, vector<bool>& rdiag, int row, int n) {
    if (row == n) {
        ans.push_back(board);
        return;
    }
    for (int i = 0; i < n; ++i) {
        if (column[i] || ldiag[n-row+i-1] || rdiag[row+i+1]) {
            continue;
        }
        // 修改当前节点状态
        board[row][i] = 'Q';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i+1] = true;
        // 递归子节点
        backtracking(ans, board, column, ldiag, rdiag, row+1, n);
        // 回改当前节点状态
        board[row][i] = '.';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i+1] = false;
    }
}

// 主函数
vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> ans;
    if (n == 0) {
        return ans;
    }
    vector<string> board(n, string(n, '.'));
    vector<bool> column(n, false), ldiag(2*n-1, false), rdiag(2*n-1, false);
    backtracking(ans, board, column, ldiag, rdiag, 0, n);
    return ans;
}

bool isBipartitle(vector<vector<int>>& graph) {
    int n = graph.size();
    if (n == 0) {
        return true;
    }
    vector<int> color(n, 0);
    queue<int> q;
    for (int i = 0; i < n; ++i) {
        if (!color[i]) {
            q.push(i);
            color[i] = 1;
        }
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (const int & j: graph[node]) {
                if (color[j] == 0) {
                    q.push(j);
                    color[j] = color[node] == 2 ? 1 : 2;
                } else if (color[node] == color[j]) {
                    return false;
                }
            }
        }
    }
    return true;
}

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> graph(numCourses, vector<int>());
    vector<int> indegree(numCourses, 0), res;
    for (const auto & prerequisite: prerequisites) {
        graph[prerequisite[1]].push_back(prerequisite[0]);
        ++indegree[prerequisite[0]];
    }
    queue<int> q;
    for (int i = 0; i < indegree.size(); ++i) {
        if (!indegree[i]) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        int u = q.front();
        res.push_back(u);
        q.pop();
        for (auto v: graph[u]) {
            --indegree[v];
            if (!indegree[v]) {
                q.push(v);
            }
        }
    }
    for (int i = 0; i < indegree.size(); ++i) {
        if (indegree[i]) {
            return vector<int>();
        }
    }
    return res;
}

unsigned int GetListLength(ListNode* pHead) {
    unsigned int nLength = 0;
    ListNode* pNode = pHead;
    while (pNode != NULL) {
        ++nLength;
        pNode = pNode->m_pNext;
    }
    return nLength;
}

ListNode* FindFirstCommonNode(ListNode* pHead1, ListNode* pHead2) {
    // 得到两个链表的长度
    unsigned int nLength1 = GetListLength(pHead1);
    unsigned int nLength2 = GetListLength(pHead2);
    int nLengthDif = nLength1 - nLength2;
    
    ListNode* pListHeadLong = pHead1;
    ListNode* pListHeadShort = pHead2;
    if (nLength2 > nLength1) {
        pListHeadLong = pHead2;
        pListHeadShort = pHead1;
        nLengthDif = nLength2 - nLength1;
    }
    
    // 先在长链表上走几步，再同时在两个链表上遍历
    for (int i = 0; i < nLengthDif; ++i) {
        pListHeadLong = pListHeadLong->m_pNext;
    }
    
    while ((pListHeadLong != NULL) && (pListHeadShort != NULL) && (pListHeadLong != pListHeadShort)) {
        pListHeadLong = pListHeadLong->m_pNext;
        pListHeadShort = pListHeadShort->m_pNext;
    }
    
    // 得到第一个公共结点
    ListNode* pFirstCommondNode = pListHeadLong;
    
    return pFirstCommondNode;
}

char FirstNotRepeatingChar(char *pString) {
    if (pString == NULL) {
        return '\0';
    }
    const int tableSize = 256;
    unsigned int hashTable[tableSize];
    for (unsigned int i = 0; i < tableSize; ++i) {
        hashTable[i] = 0;
    }
    
    char* pHashKey = pString;
    while (*pHashKey !='\0') {
        hashTable[*pHashKey]++;
        pHashKey++;
    }
    
    pHashKey = pString;
    while (*pHashKey !='\0') {
        if (hashTable[*pHashKey] == 1) {
            return *pHashKey;
        }
        pHashKey++;
    }
    return '\0';
}

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    vector<TreeNode*> m_vChildren;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};



// 最低公共祖先
bool GetNodePath(TreeNode* pRoot, TreeNode* pNode, list<TreeNode*>& path) {
    if (pRoot == pNode) {
        return true;
    }
    path.push_back(pRoot);
    
    bool found = false;
    
    vector<TreeNode*>::iterator i = pRoot->m_vChildren.begin();
    while (!found && i < pRoot->m_vChildren.end()) {
        found = GetNodePath(*i, pNode, path);
        ++i;
    }
    
    if (!found) {
        path.pop_back();
    }
    
    return found;
}

TreeNode* GetLastCommonNode(const list<TreeNode*>& path1, const list<TreeNode*>& path2) {
    list<TreeNode*>::const_iterator iterator1 = path1.begin();
    list<TreeNode*>::const_iterator iterator2 = path2.begin();
    
    TreeNode* pLast = NULL;
    while (iterator1 != path1.end() && iterator2 != path2.end()) {
        if (*iterator1 == *iterator2) {
            pLast = *iterator1;
        }
        iterator1++;
        iterator2++;
    }
    
    return pLast;
}

TreeNode* GetLastCommonParent(TreeNode* pRoot, TreeNode* pNode1, TreeNode* pNode2) {
    if (pRoot == NULL || pNode1 == NULL || pNode2 == NULL) {
        return NULL;
    }
    
    list<TreeNode*> path1;
    GetNodePath(pRoot, pNode1, path1);
    
    list<TreeNode*> path2;
    GetNodePath(pRoot, pNode2, path2);
    
    return GetLastCommonNode(path1, path2);
}


int helper(TreeNode *root) {
    if (!root) {
        return 0;
    }
    int left = helper(root->left), right = helper(root->right);
    if (left == -1 || right == -1 || abs(left - right) > 1) {
        return -1;
    }
    return 1 + max(left, right);
}

bool isBalanced(TreeNode *root) {
    return helper(root) != -1;
}

int helper(TreeNode* node, int& diameter) {
    if (!node) {
        return 0;
    }
    int l = helper(node->left, diameter);
    int r = helper(node->right, diameter);
    diameter = max(l + r, diameter);
    return max(l, r) + 1;
}

int diameterOfBinaryTree(TreeNode* root) {
    int diameter = 0;
    helper(root, diameter);
    return diameter;
}

int pathSumStartWithRoot(TreeNode* root, int sum) {
    if (!root) {
        return 0;
    }
    int count = root->val == sum ? 1 : 0;
    count += pathSumStartWithRoot(root->left, sum - root->val);
    count += pathSumStartWithRoot(root->right, sum - root->val);
    return count;
}

int pathSum(TreeNode* root, int sum) {
    return root ? pathSumStartWithRoot(root, sum) +
    pathSum(root->left, sum) + pathSum(root->right, sum) : 0;
}

bool isSymmetric(TreeNode* left, TreeNode* right) {
    if (!left && !right) {
        return true;
    }
    if (!left || !right) {
        return false;
    }
    if (left->val != right->val) {
        return false;
    }
    return isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left);
}

bool isSymmetric(TreeNode *root) {
    return root ? isSymmetric(root->left, root->right) : true;
}

TreeNode* helper(TreeNode* root, unordered_set<int>& dict, vector<TreeNode*>& forest) {
    if (!root) {
        return root;
    }
    root->left = helper(root, dict, forest);
    root->right = helper(root, dict, forest);
    if (dict.count(root->val)) {
        if (root->left) {
            forest.push_back(root->left);
        }
        if (root->right) {
            forest.push_back(root->right);
        }
        root = NULL;
    }
    return root;
}

vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
    vector<TreeNode*> forest;
    unordered_set<int> dict(to_delete.begin(), to_delete.end());
    root = helper(root, dict, forest);
    if (root) {
        forest.push_back(root);
    }
    return forest;
}

vector<double> averageOfLevels(TreeNode* root) {
    vector<double> ans;
    if (!root) {
        return ans;
    }
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int count = q.size();
        double sum = 0;
        for (int i = 0; i < count; ++i) {
            TreeNode* node = q.front();
            q.pop();
            sum += node->val;
            if (node->left) {
                q.push(node->left);
            }
            if (node->right) {
                q.push(node->right);
            }
        }
        ans.push_back(sum / count);
    }
    return ans;
}

vector<int> preorderTraversal(TreeNode* root) {
    vector<int> ret;
    if (!root) {
        return ret;
    }
    stack<TreeNode*> s;
    s.push(root);
    while (!s.empty()) {
        TreeNode* node = s.top();
        s.pop();
        ret.push_back(node->val);
        if (node->right) {
            s.push(node->right);// 先右后左，保证左子树先遍历
        }
        if (node->left) {
            s.push(node->left);
        }
    }
    return ret;
}

void printAllString(char* str) {
    int length = strlen(str);
    if (!length) {
        return;
    }
    if (length > 100) {
        cout << "字符串长度不能大于100" << endl;
        return;
    }
    int size = 8;
    char* pStr = str;
    int stringSize = 0;
    int yuCount = length % size;
    // int stringCount = length % size == 0 ? length / size : length / size + 1;
    while (*pStr != '\0') {
        stringSize++;
        if (stringSize % size == 0) {
            printf("%c", '\n');
            printf("%c", *pStr);
        } else {
            printf("%c", *pStr);
        }
        pStr++;
    }
    for (int i = 0; i < size - yuCount; ++i) {
        printf("%c", '0');
    }
    
}


int main(int argc, const char * argv[]) {
    
    int* m = additon(1, 2);
    int n = operation(3, *m, minus2);
    cout << "n:" << n <<endl;
    
    int ar[4] = {2, 7, 11, 15};
    vector<int> vec(ar, ar + 4);
    vector<int> sum = twoSum(vec, 9);
    for (auto it = sum.begin(); it != sum.end(); ++it) {
        cout << *it << ",";
    }
    cout<<endl;
    
    int mm = 3, nn = 3;
    int arr12[6] = {1, 2, 3, 0, 0, 0};
    vector<int> vec3(arr12, arr12 + mm + nn);
    
    int arr2[3] = {2, 5, 6};
    vector<int> vec33(arr2, arr2 + nn);
    
    mergeArray(vec3, mm, vec33, nn);
    
    for (auto it = vec3.begin(); it != vec3.end(); ++it) {
        cout << *it << ",";
    }
    cout<<endl;
    
    // 3 2 0 -4 2
    ListNodeP* p1 = new ListNodeP(3);
    ListNodeP* p2 = new ListNodeP(2);
    ListNodeP* p3 = new ListNodeP(0);
    ListNodeP* p4 = new ListNodeP(-4);
    ListNodeP* p5 = new ListNodeP(2);
    
    p1->next = p2;
    p2->next = p3;
    p3->next = p4;
    p4->next = p5;
    p5->next = p3;
    
    ListNodeP* startNode = detectCycle(p1);
    cout << startNode->val << endl;
    
    string minString = minWindow("ADOBECODEBANC", "ABC");
    cout << "minString:" << minString <<endl;
    
    vector<int> searchVector = vector<int>{5, 7, 7, 8, 8, 10};
    vector<int> searRange = searchRange(searchVector, 8);
    
    for (auto it = searRange.begin(); it != searRange.end(); ++it) {
        cout << *it << ",";
    }
    cout<<endl;
    
    vector<int> findVector = vector<int>{2, 5, 6, 0, 0, 1, 2};
    bool find = search(findVector, 0);
    cout << "find:" << find << endl;
    
    cout << "climbStairs:" << climbStairs(3) << endl;
    cout << "_climbStairs:" << _climbStairs(3) << endl;
    
    vector<int> robVector = vector<int>{2, 7, 9, 3, 1};
    int maxRobMoney = rob(robVector);
    cout << "maxRob:" << maxRobMoney << endl;
    
   
    vector<vector<int>> twoVector;
    for (int i = 0; i < 3; i++) {
        twoVector.push_back(vector<int>());
    }
    twoVector[0].push_back(1);
    twoVector[0].push_back(3);
    twoVector[0].push_back(1);
    twoVector[1].push_back(1);
    twoVector[1].push_back(5);
    twoVector[1].push_back(1);
    twoVector[2].push_back(4);
    twoVector[2].push_back(2);
    twoVector[2].push_back(1);
    
    int mPathSum =  minPathSum(twoVector);
    cout << "minPathSum:" << mPathSum << endl;
    
    int _mPathSum =  _minPathSum(twoVector);
    cout << "_minPathSum:" << _mPathSum << endl;
    
    vector<vector<int>> zDistanceVector = { {0, 0, 0}, {0, 1, 0}, {1, 1, 1} };
    vector<vector<int>> zeroVector;
    for (int i = 0; i < 3; i++) {
        zeroVector.push_back(vector<int>());
    }
    zeroVector[0].push_back(0);
    zeroVector[0].push_back(0);
    zeroVector[0].push_back(0);
    zeroVector[1].push_back(0);
    zeroVector[1].push_back(1);
    zeroVector[1].push_back(0);
    zeroVector[2].push_back(1);
    zeroVector[2].push_back(1);
    zeroVector[2].push_back(1);
    
    vector<vector<int>> distanceVector = updateMartix(zDistanceVector);
    for (vector<vector<int>>::iterator it = distanceVector.begin(); it != distanceVector.end(); it++) {
        for (vector<int>::iterator itit = (*it).begin(); itit != (*it).end(); itit++) {
            cout << *itit << " " << ends;
        }
        cout << endl;
    }
    
    vector<vector<char>> squareVector = { {'0', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'} };
    int square = maximalSquare(squareVector);
    cout << "square:" << square << endl;
    
    cout << "numSquares:" << numSquares(13) << endl;
    
    cout << "numDecodings:" << numDecodings("226") << endl;
    
    cout << "numDecodings:" << numDecodings("227") << endl;
    
    vector<string> wordVector = {"apple", "pen"};
    bool wordDict = wordBreak("applepenapple", wordVector);
    cout << "wordDict:" << wordDict << endl;
    
    vector<int> LISVector = {10,9,2,5,3,7,101,18};
    int lengthLIS = lengthOfLIS(LISVector);
    cout << "lengthLIS:" << lengthLIS << endl;
    
    int longestSeq = longestCommonSubsequence("abcde", "ace");
    cout << "longestSeq:" << longestSeq << endl;
    
    vector<int> partVector = {1,5,11,5};
    bool canPart = canPartition(partVector);
    cout << "canPart:" << canPart << endl;
    
    bool _canPart = _canPartition(partVector);
    cout << "_canPart:" << _canPart << endl;
    
    vector<string> formVector = {"10", "0001", "111001", "1", "0"};
    int formCount = findMaxForm(formVector, 5, 3);
    cout << "formCount:" << formCount << endl;
    
    vector<int> coinVector = {1,2,5};
    int minCoinCount = coinChange(coinVector, 11);
    cout << "minCoinCount:" << minCoinCount << endl;
    
    int minDis = minDistance("horse", "ros");
    cout << "minDis：" << minDis << endl;
    
    vector<int> sellVector = {7,1,5,3,6,4};
    int sell = maxProfit(sellVector);
    cout << "sell：" << sell << endl;
    
//    vector<int> quickSortVector = {10,9,2,5,3,7,101,18};
//    quick_sort(quickSortVector, 0, quickSortVector.size()-1);
//    for (auto it = quickSortVector.begin(); it != quickSortVector.end(); ++it) {
//        cout << *it << " ";
//    }
//    cout << endl;
    char str_[] = "Hello" ;
    char *p = str_;
    int nen = 10;
     
    printf("sizeof(%s):%lu\n", str_, sizeof(str_));
    printf("sizeof(%c):%lu\n", *p, sizeof(p));
    printf("sizeof(%d):%lu\n", nen, sizeof(nen));
    
//    Test2();
//    Test();
//    _Test();
//    Test_();
    
//    char strSrc[] = "Hello, World!\nyyyy";   //要被复制的源字符串
//    char strDest[20];                  //要复制到的目的字符数组
//    strcpy(strDest, strSrc);
//    printf("strDest: %s\n", strDest);
    
    char strdest[20];
    int leng = strlen(_strcpy(strdest, "hello world"));
    printf("len:%d", leng);
    
    sort();
    
    vector<int> kthVector = {3,2,1,5,6,4};
    int kth = findKthLargetst(kthVector, 2);
    cout << "kth:" << kth << endl;
    
    vector<int> bucketVector = {1,1,1,1,2,2,3,4};
    vector<int> topKF = topKFrequent(bucketVector, 2);
    for (auto it = topKF.begin(); it != topKF.end(); it++) {
        cout << *it << " " << ends;
    }
    cout << endl;
    
    
    vector<vector<int>> gridVector = { {1,0,1,1,0,1,0,1}, {1,0,1,1,0,1,1,1}, {0,0,0,0,0,0,0,1} };
    int maxArea = maxAreaOfIsland(gridVector);
    cout << "maxArea:" << maxArea << endl;
    
    vector<int> permVector = {1,2,3};
    vector<vector<int>> pVector = permute(permVector);
    for (auto it = pVector.begin(); it != pVector.end(); it++) {
        for (auto itit = (*it).begin(); itit != (*it).end(); itit++) {
            cout << *itit << " " << ends;
        }
        cout << endl;
    }
    
    vector<vector<int>> combinVector = combine(4, 2);
    for (auto it = combinVector.begin(); it != combinVector.end(); it++) {
        for (auto itit = (*it).begin(); itit != (*it).end(); itit++) {
            cout << *itit << " " << ends;
        }
        cout << endl;
    }
    
    cout << endl;
    vector<vector<string>> nQueensVector = solveNQueens(4);
    for (auto it = nQueensVector.begin(); it != nQueensVector.end(); it++) {
        for (auto itit = (*it).begin(); itit != (*it).end(); itit++) {
            cout << *itit << " " << endl;
        }
        cout << endl;
    }
    
    vector<int> diameterVector = {1,2,3,4,5};
    
    char *pString = "abaccdeff";
    char notRepeatChar = FirstNotRepeatingChar(pString);
    printf("notRepeatChar:%c\n", notRepeatChar);
    
    char *pStr = "0abc0  ";
    printAllString(pStr);
    printf("\n");
    
    vector<int> v2; // 构造一个空的vector
    vector<int> v11(5, 42); // 构造了一个包含5个值为42的元素的vector
    int back = v11.back();
    int capacity = v11.capacity();
    bool empty = v2.empty();
    int va = v11.at(1);
    v11.erase(v11.begin());
    v11.erase(v11.begin(), v11.end());
    
    
    
    
    
    int x;
    int y;
    int z;
    int pp;
    
//    int * p1 = &x;// 指针可以被修改，值也可以被修改
//    const int * p2 = &y; // 指针可以被修改，值不可以被修改(const int)
//    int * const p3 = &z; // 指针不可以被修改(* const)，值可以被修改
//    const int * const p4 = &pp; // 指针不可以被修改，值也不可以被修改
    
//    x = 24;
//    y = 34;
//    z = 44;
//    pp = 55;
//
//    *p1 = 6;
//    *p2 = z;
//    *p3 = 33;
//    *p4 = pp;
    
    
    AA a22;
    a22.Print();
    
    Solution solution;
    cout<<solution.isLegalIP("129.45.354.34")<<endl;
    cout<<solution.isLegalIP("129.45.54.34")<<endl;
    cout<<solution.isLegalIP("329.45.54.34")<<endl;
    
//    int *ptr = const_cast<int *>(fun(2,3));
    
    string str88 = "012345678";
    
    //求出字符串的长度
    int len8 = str88.length();
    
    for (int i = 0; i<len8/2; i++)
    {
        //前后交换
        char temp = str88[i];
        str88[i] = str88[len8-i-1];
        str88[len8-i-1] = temp;
    }
    
    //输出交换后的字符串
    cout<<str88<<endl;
    
    
    double d1, d2;
    d1 = 1.001;
    d2 = 1.0001;
    cout << equal(d1, d2) << endl;    // 由于精度原因不能用等号判断两个小数是否相等。
    // 判断两个小数是否相等，只能判断他们之差的绝对值是不是在一个很小的范围内。比如小于0.0000001
    
    cout<<Power(2, 8)<<endl;
    cout<<Power(2, 0)<<endl;
    cout<<Power(0, 2)<<endl;
    cout<<Power(0, -2)<<endl;
    cout<<Power(2, -3)<<endl;
    // 判断g_InvalidInput
    
    cout<<NumberOf1(11)<<endl;
    cout<<NumberOf1(-11)<<endl;
    cout<<NumberOf1InBinary(12)<<endl;
    cout<<NumberOf1InBinary(-12)<<endl;
    
    cout<<AddFrom1ToN_Recursive(101819)<<endl; // 当数据够大时，会调用栈会溢出。 递归时，内存栈中分配空间以保存参数，返回地址，临时变量等，而且往栈中压人数据和弹出数据都需要时间，每个进程栈容量有限 空间和时间消耗
    cout<<AddFrom1ToN_Iterative(101819)<<endl;
    
    // 快速排序
    int arr[] = {1, 57, 68, 59, 52, 72, 28, 96, 33, 24};
    Qsort(arr, 0, sizeof(arr) / sizeof(arr[0]) - 1);/*这里原文第三个参数要减1否则内存越界*/
    
    for(int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        cout << arr[i] << " ";
    }
    
//    QuickSort(arr, 9, 0, 8);
//    for (int i = 0; i < 9; i++) {
//        cout<<" "<<arr[i]<<",";
//    }
    cout<<endl;
    int ages[] = {1, 57, 68, 59, 52, 52, 57, 25, 34, 25, 24, 23, 24, 72, 28, 96, 33, 24, 25, 25};
    SortAges(ages, sizeof(ages) / sizeof(ages[0]));
    
    for(int i = 0; i < sizeof(ages) / sizeof(ages[0]); i++)
    {
        cout << ages[i] << " ";
    }
    
    cout<<endl;
    
//    int arr2[] = {6, 8, 9, 11, 1, 1, 2, 5};
//    int arr3[] = {1, 0, 1, 1, 1}; // {1, 1, 1, 0, 1}
    int arr3[] = {1, 1, 1, 0, 1};
    int minNm = MinNumber(arr3, sizeof(arr3)/sizeof(arr3[0]));
    cout<<"最小数字为:"<<minNm;
    
    cout<<endl;
    
    CStack<int> stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    
    int len=4;
    while(len>0)
    {
        cout<<stack.pop()<<" ";
        --len;
    }
    
    cout<<endl;
    
    CQueue<int> queue;
    queue.appendtail(1);
    queue.appendtail(2);
    queue.appendtail(3);
    queue.appendtail(4);
    len=4;
    while(len>0)
    {
        cout<<queue.deleteHead()<<endl;
        --len;
    }
    system("pause");
    
    int a[][4] = {{1,2,8,9},{2,4,9,5},{4,7,10,13},{6,8,11,15}};
    cout << findMatrix((int *)a, 4, 4, 11) <<endl;
    
    char str[16] = "we are  happy! ";
    ReplaceBlank(str, 24);
    cout<<"str="<<str<<endl;
    
    std::cout << "Hello, World!\n";
    cout << "最大值：" << (numeric_limits<int>::max)();
    cout << "\t最小值：" << (numeric_limits<int>::min)() << endl;
    printf("%d\n", atoi("2147483648"));
    printf("%d\n", atoi("2147483647"));
    printf("%d\n", atoi("-2147483648"));
    printf("%d\n", atoi("-2147483649"));
    
    char strSrc[] = "Hello, World!\nyyyy";   //要被复制的源字符串
    char strDest[20];                  //要复制到的目的字符数组

    strcpy(strDest, strSrc);
    printf("strDest: %s\n", strDest);
    /*
    memcpy(strDest, strSrc, 4);    //复制strSrc的前4个字符到strDest中
    strDest[4] = '\0';             //把strDest的第5个元素赋为结束符'\0'
    printf("strDest: %s\n", strDest);
     */
    
//    Hello, World!
//    12345
//strDest: Hello, World!
//    yyyy
//strDest: Hell
    
    /*
    int i;
    for(i=0; i<2; i++){
        fork();
        printf("g");
    }
    
    wait(NULL);
    wait(NULL);
// gggggggg
    
    for(i=0; i<2; i++){
        fork();
        printf("\ng  ppid=%d, pid=%d, i=%d \n", getppid(), getpid(), i);
    }
    
    wait(NULL);
    wait(NULL);
    
    printf("\nstart the dead loop\n");
//    while(1)
//    {
//        printf("/b->");
//        fflush(stdout);//刷新输出缓冲区
//        usleep(100000);
//    }
     */
    
    
    //创建结点
    ListNode* pNode1=CreateListNode(1);//创建一个结点
    PrintList(pNode1);//打印
    //往链表中添加新结点
    AddToTail(&pNode1,2);//为链表添加一个结点
    AddToTail(&pNode1,3);//为链表添加一个结点
    AddToTail(&pNode1,4);//为链表添加一个结点
    AddToTail(&pNode1,5);//为链表添加一个结点
    AddToTail(&pNode1,6);//为链表添加一个结点
    AddToTail(&pNode1,7);//为链表添加一个结点
    //打印链表
    PrintList(pNode1);//打印
    //反转链表
    ListNode* pReversedHead=ReverseList(pNode1);
    PrintList(pReversedHead);//打印
    
    system("pause");
    
    
    //            10
    //         /      \
    //        6        14
    //       /\        /\
    //      4  8     12  16
    //创建树结点
    BinaryTreeNode *pNode10 = CreateBinaryTreeNode(10);
    BinaryTreeNode *pNode6 = CreateBinaryTreeNode(6);
    BinaryTreeNode *pNode14 = CreateBinaryTreeNode(14);
    BinaryTreeNode *pNode4 = CreateBinaryTreeNode(4);
    BinaryTreeNode *pNode8 = CreateBinaryTreeNode(8);
    BinaryTreeNode *pNode12 = CreateBinaryTreeNode(12);
    BinaryTreeNode *pNode16 = CreateBinaryTreeNode(16);
    //连接树结点
    ConnectTreeNodes(pNode10, pNode6, pNode14);
    ConnectTreeNodes(pNode6, pNode4, pNode8);
    ConnectTreeNodes(pNode14, pNode12, pNode16);
    
    InOrderPrintTree(pNode10);//中序遍历
    BinaryTreeNode *pHeadOfList=Convert(pNode10);//获取双向链表头结点
    PrintList(pHeadOfList);//输出链表
    
    system("pause");
    
    char string[] = "abcde";
    size_t length = strlen(string);
    Permutation(string, 0, length-1);
    
    vector<int> v1;
    
    vector<int>::iterator Iter;
    v1.push_back(10);
    v1.push_back(20);
    v1.push_back(30);
    v1.push_back(40);
    v1.push_back(50);
    v1.push_back(10);
//    v1.push_back(50);
    cout<<"v1=" ;
    for (Iter = v1.begin(); Iter != v1.end(); Iter++) {
        cout<<" "<<*Iter;
    }
    cout<<endl;
    v1.erase(v1.begin());
    cout<<"v1=";
    for (Iter = v1.begin(); Iter != v1.end(); Iter++) {
        cout<<" "<<*Iter;
    }
    
    // 1.第一种方案
    /*
    for(Iter = v1.begin(); Iter != v1.end(); Iter++)
    {
        if(*Iter == 10)
        {
            v1.erase(Iter);  // 如果最后一个元素为10，删除最后一个10时，返回值为下一个元素，而下一个元素没有了，导致迭代器失效变为野指针，需要把旧容器整成新的容器
//            Iter = v1.begin(); // 当erase后，旧的容器会被重新整理成一个新的容器
        }
    }
     */
    
    for(Iter = v1.begin(); Iter != v1.end(); Iter++)
    {
        if(*Iter == 10)
        {
            Iter = v1.erase(Iter);//Iter为删除元素的下一个元素的迭代器
            //即第一次这段语句后Iter 会是20，大家可以通过debug调试出来查看下数值
        }
        
        if(Iter == v1.end()) //要控制迭代器不能超过整个容器
        { 
            break;
        } 
    }
    
    cout<<endl;
    cout<<"v1=";
    for (Iter = v1.begin(); Iter != v1.end(); Iter++) {
        cout<<" "<<*Iter;
    }
    
    cout<<endl;
    vector<int>::iterator itera = v1.erase(v1.begin()+1, v1.begin()+3);
    cout<<" "<<*itera<<endl; // 返回值是一个迭代器，指向删除元素下一个元素
    cout<<"v1=";
    for (Iter = v1.begin(); Iter != v1.end(); Iter++) {
        cout<<" "<<*Iter;
    }
    cout<<endl;
    
    int k;
    float f;
    f = (float)k;
    f = static_cast<float>(k);
    
    // 2.const_case
    
    
//    A<int> a;
//    cout<<a.g(2, 5)<<endl;
    
//    double *a;
//    double *b;
//    double a1 = 4.74;
//    double b1 = 5.43;
//    a = &a1;
//    b = &b1;
//    Swap(a, b);
//    
//    cout<<"a="<<*a<<" "<<"b="<<*b<<endl;
//    
//    int i = 10;
//    int j = 30;
//    cout<< "i, j= "<<i<<", "<<j<<".\n";
//    Swap(i,j);
//    cout<<"now i, j = "<<i<<","<<j<<".\n";
    
    
    
    
    
    return 0;
}


class _String
{
public:
    _String(const char *str = NULL);
    _String(const _String &other);
    ~ _String(void);
    _String & operator = (const _String &other);
private:
    char *m_data;
};

_String::~_String(void)
{
    delete m_data;
    m_data = NULL;
}

_String::_String(const char *str)
{
    if (str == NULL) {
        m_data = new char[1]; // 若能加 NULL 判断则更好
        *m_data = '\0';
    } else {
        int length = strlen(str);
        m_data = new char[length+1]; // 若能加 NULL 判断则更好
        strcpy(m_data, str);
    }
}

// 拷贝构造函数
_String::_String(const _String &other)
{
    int length = strlen(other.m_data);
    m_data = new char[length+1]; // 若能加 NULL 判断则更好
    strcpy(m_data, other.m_data);
}

// 赋值函数
_String & _String::operator=(const _String &other)
{
    // 检查自赋值
    if (this == &other) {
        return *this;
    }
    // 释放原有的内存资源
    delete [] m_data;
    m_data = NULL;
    // 分配新的内存资源，并复制内容
    int length = strlen(other.m_data);
    m_data = new char[length+1]; // 若能加 NULL 判断则更好
    strcpy(m_data, other.m_data);
    // 返回本对象的引用
    return *this;
}

```


























