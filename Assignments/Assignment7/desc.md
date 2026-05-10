The Bajillion Search Engine
Bajillion 搜索引擎
In 1998, two Stanford CS graduate students, Larry Page and Sergey Brin, founded Google Inc. to provide a new way of doing search on the Internet based on research they had conducted as part of the Stanford Digital Libraries project. If you're interested, you can find their original paper describing the initial version of the Google search engine here:
1998 年，斯坦福大学两名计算机科学研究生拉里·佩奇和谢尔盖·布林创立了谷歌公司，旨在基于他们在斯坦福数字图书馆项目中进行的研究，为互联网提供一种新的搜索方式。如果你感兴趣，可以在这里找到他们描述谷歌搜索引擎初版的原始论文：

http://infolab.stanford.edu/~backrub/google.html

As their paper explains, the original URL (Uniform Resource Locator, or web address) for Google was in fact hosted at Stanford: http://google.stanford.edu/. Ironically enough, that URL now redirects to a web site describing the G Suite software tools that Stanford licenses from Google, Inc.
正如他们的论文所解释的那样，谷歌最初的 URL（统一资源定位符，或网址）实际上托管在斯坦福大学：http://google.stanford.edu/。说来也讽刺，现在这个 URL 已经重定向到一个网站，该网站描述了斯坦福大学从谷歌公司获得许可的 G Suite 软件工具。

What you might not know is that sigificant portions of the original version of the Google were written in Python. You can find more details about that in the paper referenced above. In fact, it turns out that writing a simple search engine in Python is entirely doable given the knowledge that you now have in CS106A! To prove that point, in this assignment you'll will be implementing your own text-based search engine. It's like Google, only smaller. Much, much, smaller.
你可能不知道的是，谷歌原始版本的很大一部分是用 Python 编写的。你可以在上面提到的论文中找到更多细节。事实上，结果表明，凭借你在 CS106A 课程中学到的知识，用 Python 编写一个简单的搜索引擎完全是可行的！为了证明这一点，在这个作业中，你将实现自己的基于文本的搜索引擎。它就像谷歌一样，只是规模更小。小得多，小得多。

The name Google comes from the term "googol", which refers to the number formed by a 1 followed by 100 zeroes (or, equivalently, 10 to the 100th power). The name of the company Google actually comes from an unintentional misspelling of the term googol, as Larry Page wanted the name to refer to a really large number. Since the name "google" is already taken, we figured you could name your search engine after another notion of a really large number, which is why your search engine is called "Bajillion." As in, "there are a bajillion things I've learning in CS106A this quarter!"
Google 这个名字来源于“googol”这个词，它指的是一个 1 后面跟着 100 个零的数（或者等价地，10 的 100 次方）。Google 公司的名字实际上来源于“googol”这个词的无意拼写错误，因为 Larry Page 希望这个名字能指一个非常大的数。由于“google”这个名字已经被占用，我们觉得你可以用另一个表示非常大的数的概念来命名你的搜索引擎，这就是为什么你的搜索引擎被称为“Bajillion”。也就是说，“我这季度在 CS106A 学到了无数的东西！”

There are two main parts of the search engine that you'll be implementing. The first, which is the heart of the search engine, is called the "index," which is described in Part A below and the second is the actual search functionality, which is described in Part B.
搜索引擎主要包含两个部分，你将实现这两个部分。第一个，作为搜索引擎的核心，被称为“索引”，在下面的 A 部分中描述，第二个是实际搜索功能，在 B 部分中描述。

Part A: The Index
A 部分：索引
Most search engines are built on top of what is called an "inverted index," or just "index" for short. An index for a search engine is similar to the index of words in the back of book. Basically, it tells you the page (or, in the more general case, the document or file) where each word appears.
大多数搜索引擎都是基于一种称为“倒排索引”的技术构建的，通常简称为“索引”。搜索引擎的索引类似于书后所附的单词索引。基本上，它告诉你每个单词出现在哪一页（或者，在更一般的情况下，出现在哪个文档或文件中）。

In search, we use the notion of a "term" to refer to generalized notion of a word, name, number, etc. that we might want to look up in a collection of documents. If it's easier, you can just think of a "term" as a "word", but really it could refer to something like the number "127" which is not officially a "word".
在搜索中，我们使用“术语”的概念来指代一个通用的概念，比如单词、名称、数字等，我们可能希望在文档集合中查找的内容。如果更容易理解，你可以简单地将“术语”视为“单词”，但实际上它可能指代像数字“127”这样的内容，而“127”并非正式的“单词”。

In any case, an index is structure where, for each term, we have a list of the documents that this term appears in. Consider the following expository examples of terms and documents they appear in:
无论如何，索引是一种结构，其中对于每个术语，我们都有一个该术语出现在其中的文档列表。以下是术语及其出现的文档的一些说明性示例：

The term "burrito" appears in the text documents named "recipes.txt", "greatest eats.txt", "top 10 foods.txt", and "favs.txt"
"burrito" 这个词出现在名为 "recipes.txt"、"greatest eats.txt"、"top 10 foods.txt" 和 "favs.txt" 的文本文件中
The term "sushi" appears in the text documents "favs.txt" and "Japanese foods.txt"
"sushi" 这个词出现在文本文件 "favs.txt" 和 "Japanese foods.txt" 中
The term "samosa" appears in the text document "appetizers.txt"
"samosa" 这个词出现在文本文件 "appetizers.txt" 中
We could represent an index of these terms as something like:
我们可以将这些词表示为一个索引，例如：

"burrito" → "recipes.txt", "greatest eats.txt", "top 10 foods.txt", and "favs.txt"
"sushi"   → "favs.txt" and "Japanese foods.txt"
"samosa"  → "appetizers.txt"
If we wanted to represent such a mapping from terms to a list of documents (file names) in Python, a dictionary would be a natural structure to use. Thus, the index could be represented as the following Python dictionary:
如果我们想在 Python 中表示从术语到文档列表（文件名）的映射，字典将是一个自然的数据结构。因此，索引可以表示为以下 Python 字典：

index = {
  'burrito': ['recipes.txt', 'greatest eats.txt', 'top 10 foods.txt', 'favs.txt'], 
  'sushi': ['favs.txt', 'Japanese foods.txt'],
  'samosa': ['appetizers.txt']
}
Note that in the dictionary above, the terms (strings) are the keys, and the values are lists of the names of files containing those terms (the file names are strings).
请注意，在上述字典中，术语（字符串）是键，值是包含这些术语的文件名列表（文件名是字符串）。

Building an index  构建索引
Your task in this part of the assignment is to write the code the builds an index for a set of text files. More specifically, you will be implementing a function:
在这个作业的这部分，你的任务是编写构建文本文件集索引的代码。更具体地说，你将实现一个函数：

create_index(filenames, index, file_titles)
This function is passed the following information:
此函数接收以下信息：

filenames: this is a list of file names (strings) that you'll use in building an index.
filenames : 这是一个你将用于构建索引的文件名（字符串）列表。
index: this is a dictionary representing the index that you will need to build up. When your function is called, it will be passed an empty dictionary ({}) for index. Since dictionaries are mutable types, any changes your function makes to the parameter index will persist after your function completes.
index : 这是一个表示索引的字典，你需要构建它。当你的函数被调用时，它将传递一个空的字典（{}）给 index。由于字典是可变类型，你的函数对参数 index 做出的任何更改在函数完成后都会持续存在。
file_titles: this is a dictionary where the keys are file names (strings) and the values are the titles of the articles in each file (which are also strings). We'll explain the details of this parameter later in this handout. When your function is called, it will be passed an empty dictionary ({}) for file_titles and your function will add entries to this dictionary as appropriate.
file_titles : 这是一个字典，其中键是文件名（字符串），值是每个文件中文章的标题（也是字符串）。我们将在本手册的后面详细解释此参数。当您的函数被调用时，将为 file_titles 传递一个空字典（{}），您的函数将根据需要向此字典添加条目。
You will build the index based on the set of files specified in the parameter filenames. For each file in the filenames list, you should parse out all the terms in the file in order to add appropriate entries to the index that you are building.
您将根据参数 filenames 中指定的文件集来构建索引。对于 filenames 列表中的每个文件，您应该解析出文件中的所有术语，以便向您正在构建的索引中添加适当的条目。

Terms are defined as follows:
术语定义如下：

Terms are seperated from each other in text by spaces or newline (return) characters.
术语在文本中由空格或换行（回车）字符分隔。
Terms should have all their letters converted to lowercase.
术语中的所有字母应转换为小写。
Terms should have all punctuation symbols stripped off from their beginning and end. (Punctuation characters in the middle of a term are fine and should not be removed).
术语开头和结尾的所有标点符号应被移除。（术语中间的标点符号是允许的，不应被移除）。
To help implement the third bullet point above, the Python string library (which is already imported in the starter code we give you with the line import string) provides a constant called string.punctuation, which is a string containing all the punctuation marks in Python. You can use this constant in conjunction with the strip function on strings to remove punctuation marks from just the beginning and ending of a string, as shown in the example from the Python console below:
为了帮助实现上述第三点，Python 字符串库（已经在随附的启动代码中通过 import string 导入）提供了一个名为 string.punctuation 的常量，它是一个包含所有 Python 标点符号的字符串。您可以使用这个常量与字符串的 strip 函数结合使用，以从字符串的开始和结束处删除标点符号，如下面的 Python 控制台示例所示：

>>> raw = '$$j.lo!'
>>> term = raw.strip(string.punctuation)
>>> term
'j.lo'
Recall that the strip function only removes characters from the beginning and ending of a string. strip will not remove punctuation marks in the middle of a string. Thus, in the example above, the period in the middle of 'j.lo' remains after the call to strip.
回想一下，strip 函数仅从字符串的开始和结束处移除字符。strip 不会移除字符串中间的标点符号。因此，在上面的示例中，'j.lo' 中间的句号在 strip 调用后仍然存在。

As an additional point about terms, any string of characters that only contains punctuation marks is not considered a term and should not be added to the index. In such a case, if we stripped all the punctuation from the string, we would be left with the empty string (""), and empty strings should not be included in the index.
关于术语的补充说明，任何仅包含标点符号的字符序列不被视为术语，也不应添加到索引中。在这种情况下，如果我们从字符串中移除所有标点符号，我们会得到空字符串（""），空字符串不应包含在索引中。

To make this all more concrete, say that we want to index the text file 'doc1.txt' shown below:
为了更具体地说明，假设我们想要索引下面显示的文本文件'doc1.txt'：

doc1.txt

*We* are 100,000
STRONG! $$
In parsing this file, we should produce the following terms:
在解析此文件时，我们应该生成以下术语：

The string '*We*' should be converted to term 'we'
字符串 '*我们*' 应转换为术语 '我们'
The string 'are' should be converted to term 'are'
字符串 'are' 应转换为术语 'are'
The string '100,000' should be converted to term '100,000' (Note that the comma inside 100,000 is fine and should not be removed.)
字符串 '100,000' 应转换为术语 '100,000'（注意：100,000 中的逗号是允许的，不应删除。）
The string 'STRONG!' should be converted to term 'strong'
字符串 'STRONG!' 应转换为术语 'strong'
The string '$$' should be ignored (i.e., not included in the index), as a string of only punctuation is not considered a term.
字符串'$$'应该被忽略（即不包含在索引中），因为仅由标点符号组成的字符串不被视为术语。
As you produce terms from a file, you should add appropriate entries into the index for each of the terms. For example, if we started with an index that was the empty dictionary, the index should look as follows after processing the file 'doc1.txt':
当你从文件中生成术语时，你应该为每个术语向索引中添加适当的条目。例如，如果我们从一个空字典开始作为索引，处理文件'doc1.txt'后，索引应该如下所示：

{
  'we' : ['doc1.txt'],
  'are' : ['doc1.txt'],
  '100,000' : ['doc1.txt'],
  'strong' : ['doc1.txt']
}
Say, we now process another file, 'doc2.txt', shown below:
说，我们现在处理另一个文件，'doc2.txt'，如下所示：

doc2.txt

Strong, you are!
--Yoda--
We should appropriately update the index we had before with the terms found in 'doc2.txt', we should result in the index shown below.
我们应该适当用' doc2.txt '中找到的术语更新我们之前的索引，我们应该得到下面显示的索引。

{
  'we' : ['doc1.txt'],
  'are' : ['doc1.txt', 'doc2.txt'],
  '100,000' : ['doc1.txt'],
  'strong' : ['doc1.txt', 'doc2.txt'],
  'you': ['doc2.txt'].
  'yoda': ['doc2.txt']
}
Note that in cases where a term found in 'doc2.txt' previously existed in the index (such as 'are' and 'strong'), the list of documents that contain that term was expanded to include the file 'doc2.txt'. In cases where a term found in 'doc2.txt' was not previously in the index (such as 'you' and 'yoda'), a new entry is added to the index to indicate that the given term appeared in 'doc2.txt'.
请注意，当在'doc2.txt'中找到的术语之前已存在于索引中（例如'are'和'strong'）时，包含该术语的文档列表被扩展以包含文件'doc2.txt'。当在'doc2.txt'中找到的术语之前不在索引中（例如'you'和'yoda'）时，索引中会添加一个新的条目，以指示给定的术语出现在'doc2.txt'中。

Building the dictionary file_titles
构建字典文件 titles
In real-world search engines, we often want to store additional information about each file while we are processing it in order to use this information later when we want to display search results. For example, for web pages, we might store the title of the page. For news articles, we might store the headline of the article. In the news article data we provide in this assignment, the first line of each file is a title for the article in that file, which we want to store for future reference. Here is an example of the first portion of two of the actual files (named '001.txt' and '002.txt', respectively) in the BBC News article data that we provide for you in the assignment:
在现实世界的搜索引擎中，我们通常希望在处理文件时存储有关每个文件的其他信息，以便在以后需要显示搜索结果时使用这些信息。例如，对于网页，我们可能会存储页面的标题。对于新闻文章，我们可能会存储文章的标题。在本作业中我们提供的新闻文章数据中，每个文件的第一行是该文件中文章的标题，我们希望存储它以供将来参考。以下是我们在作业中提供的 BBC 新闻文章数据中两个实际文件（分别命名为'001.txt'和'002.txt'）的第一部分示例：

[ `001.txt` ]{style="max-width:50%"} ``` {.console style="white-space: pre-wrap;"} Broadband steams ahead in the US More and more Americans are joining the internet's fast lane, according to official figures. ... ``` [ `002.txt` ]{style="max-width:50%"} ``` {.console style="white-space: pre-wrap;"} EA to take on film and TV giants Video game giant Electronic Arts (EA) says it wants to become the biggest entertainment firm in the world. ... ```
[ `001.txt` ]{style="max-width:50%"} ``` {.console style="white-space: pre-wrap;"} 美国宽带发展迅速 官方数据显示，越来越多的美国人加入了互联网的高速通道... ``` [ `002.txt` ]{style="max-width:50%"} ``` {.console style="white-space: pre-wrap;"} 电子艺界欲挑战影视巨头 游戏巨头电子艺界（EA）表示，希望成为全球最大的娱乐公司...
When we are process each file to build up the index, we also want to add an entry to the dictionary file_titles to keep track of the title for each file. Recall, that the title is simply the first line of the file (with the "newline" character at the end of the line removed). We store this information in file_titles, where the file name (string) is the key and the title (string) is the value for an entry in the dictionary.
当我们处理每个文件来构建索引时，我们也想向字典文件 titles 添加一个条目，以跟踪每个文件的标题。回想一下，标题只是文件的第一行（行末的"换行"字符被移除）。我们将这些信息存储在文件 titles 中，其中文件名（字符串）是字典中条目的键，标题（字符串）是条目的值。

So, if we started with file_titles as an empty dictionary (which is the case when your create_index function is called), after we process the files '001.txt' and '002.txt', the file_titles dictionary should look as follows:
所以，如果我们以空的 file_titles 字典开始（当你的 create_index 函数被调用时的情况），在处理文件 '001.txt' 和 '002.txt' 之后，file_titles 字典应该看起来如下：

file_titles.txt

{
 '001.txt': 'Broadband steams ahead in the US',
 '002.txt': 'EA to take on film and TV giants'
}
::: {.alert .alert-primary} Important note: the terms in the title line for each file should still be included in the index (along with the rest of the document). A common bug is to forget to add the terms from the title line to the index. :::
::: {.alert .alert-primary} 重要提示：每个文件标题行中的术语仍应包含在索引中（以及文档的其余部分）。一个常见的错误是忘记将标题行中的术语添加到索引中。 :::

Doctests for the create_index function are provided for you to test your function. Feel free to write additional doctests. Also, you should definitely write additional functions that may help you decompose your solution to this problem.
为 create_index 函数提供的 doctests 可供您测试您的函数。您可以自由编写额外的 doctests。此外，您应该绝对编写额外的函数，这些函数可能有助于您将此问题的解决方案分解。

Running your create_index function
运行你的 create_index 函数
You can run your create_index function by running the searchengine.py program and specifying the directory name for a set of text files that you would like to index. We provide two such data sets for you to test your code. The first is in a directory named small, which includes three very short text files, making the size of the resulting index manageable to inspect manually. You can run your program with the small dataset in a Python Terminal using this command (on a Mac, use python3 instead of py):
您可以通过运行 searchengine.py 程序并指定您希望索引的一组文本文件的目录名来运行您的 create_index 函数。我们为您提供两个这样的数据集用于测试您的代码。第一个是一个名为 small 的目录，其中包含三个非常短的文本文件，使得生成的索引大小适合手动检查。您可以在 Python 终端中使用以下命令运行您的程序（在 Mac 上，请使用 python3 而不是 py）：

> py searchengine.py small
In the searchengine.py program, we provide a main function that calls your create_index function and prints the resulting index and file_titles on the terminal. The output printed by the program on the small dataset, should look as shown below. (Note that the output below is produced on a mac, where file paths use the forward-slash character: '/'. On a PC, you would see a double backslash '\\' in the file paths instead of a forward-slash).
在 searchengine.py 程序中，我们提供了一个 main 函数，该函数调用您的 create_index 函数，并在终端打印生成的索引和文件标题。程序在小数据集上打印的输出应如下所示。（注意，下面输出的文件路径是在 Mac 上生成的，使用的是正斜杠字符：'/'。在 PC 上，您会看到文件路径中使用的是双反斜杠 '\\' 而不是正斜杠）。

``` {.console style="white-space: pre-wrap;"} Index: {'file1': ['small/1.txt'], 'title': ['small/1.txt', 'small/2.txt', 'small/3.txt'], 'apple': ['small/1.txt', 'small/2.txt', 'small/3.txt'], 'ball': ['small/1.txt', 'small/3.txt'], 'dog': ['small/1.txt', 'small/2.txt'], 'elephant': ['small/1.txt'], 'frog': ['small/1.txt'], 'file2': ['small/2.txt'], 'carrot': ['small/2.txt', 'small/3.txt'], 'file3': ['small/3.txt'], 'gerbil': ['small/3.txt'], 'hamster': ['small/3.txt'], 'iguana': ['small/3.txt'], 'lizard': ['small/3.txt']} File names -> document titles: {'small/1.txt': '** File1 title ', 'small/2.txt': ' File2 title ', 'small/3.txt': ' File3 title **'}
auto: ``` {.console style="white-space: pre-wrap;"} Index: {'file1': ['small/1.txt'], 'title': ['small/1.txt', 'small/2.txt', 'small/3.txt'], 'apple': ['small/1.txt', 'small/2.txt', 'small/3.txt'], 'ball': ['small/1.txt', 'small/3.txt'], 'dog': ['small/1.txt', 'small/2.txt'], 'elephant': ['small/1.txt'], 'frog': ['small/1.txt'], 'file2': ['small/2.txt'], 'carrot': ['small/2.txt', 'small/3.txt'], 'file3': ['small/3.txt'], 'gerbil': ['small/3.txt'], 'hamster': ['small/3.txt'], 'iguana': ['small/3.txt'], 'lizard': ['small/3.txt']} 文件名 -> 文档标题: {'small/1.txt': '** 文件 1 标题', 'small/2.txt': '文件 2 标题', 'small/3.txt': '文件 3 标题 **'}


When you think you\'ve gotten your program working well on the small
dataset, you can then try it out on the BBC News article dataset
^[\[1\]](#credit)^ with the following command (on the Mac, use python3
instead of py):

``` console
> py searchengine.py bbcnews
The output produced in that case is too large to verify manually, but running on such a large dataset is a good way to see if you program crashes on any cases that might have been missed with the small dataset.
在这种情况下生成的输出太大而无法手动验证，但在如此大的数据集上运行是一个好方法，可以查看你的程序是否在可能被小数据集遗漏的任何情况下崩溃。

Part B: Using the index to search
Part B: 使用索引进行搜索
Once you feel as though you are indexing documents correctly, you're ready to implement the actual search functionality. Luckily for you, many people find implementing this part of the program much easier than building an index. And, as an added bonus, you'll likely be able to leverage the common function you wrote in the first part of this assignment. Yeah, sometimes we really do plan for things to work out like that.
一旦你觉得文档索引正确无误，你就可以开始实现实际的搜索功能了。幸运的是，许多人发现实现这个程序部分比建立索引要容易得多。而且，作为一个额外的福利，你很可能能够利用在本次作业第一部分编写的一个通用函数。是的，有时候我们确实会计划事情能够顺利发展。

Your task in this part of the assignment is to write the code that implements the search functionality making use of the index you built in Part A. Specifically, you will be implementing a function:
在这个作业的这部分中，你的任务是编写代码来实现搜索功能，利用你在 A 部分构建的索引。具体来说，你将实现一个函数：

search(index, query)
This function is passed the following information:
此函数接收以下信息：

index: this is the index produced by your create_index function
索引：这是由您的 create_index 函数生成的索引
query: this is a string representing the user's query. All the letters in this string are guaranteed to be lowercase (the starter code we provide uses the lower function to create a lowercase query string that is passed to this function). To simplify things, you can assume that the user will never enter punctuation characters as part of the query string. The code we provide does not actually strip out puctuation characters from the user's query (in case you wanted to do some sort of extension where such punctuation characters might be meaningful in terms of how the search is conducted). But, you can just assume for the basic version of the program that the user will not enter any punctuation characters in their query.
查询：这是一个代表用户查询的字符串。这个字符串中的所有字母都保证是小写的（我们提供的起始代码使用 lower 函数来创建一个传递给这个函数的小写查询字符串）。为了简化问题，你可以假设用户永远不会将标点符号作为查询字符串的一部分输入。我们提供的代码实际上并不会从用户的查询中删除标点符号（以防你想做一些扩展，其中这些标点符号在搜索方式方面可能具有意义）。但是，对于程序的基本版本，你可以假设用户在他们的查询中不会输入任何标点符号。
Your search function should return a list of the names of the files that contain all of the terms in the given query. As we discussed in class, you can determine which files contain all the query terms using the index. Recall that in the index, the value associated with each term (key) is a list of the files that contain the given term. This list of files is called the "posting list" for the term. In order to determine which files contain all of the terms in a query, you start with the posting list for the first term in the query. You then consecutively consider the overlap (i.e., the common elements) of the posting list you have with the posting list associated with each subsequent term in the query. When you've processed all the terms in the query in this way, the posting list you have left should contain only those files that contain every term in the query.
您的搜索功能应该返回一个包含所有查询项的文件名称列表。正如我们在课堂上讨论的，您可以使用索引来确定哪些文件包含所有查询项。请记住，在索引中，每个词（键）关联的值是一个包含该词的文件列表。这个文件列表被称为该词的“倒排文件”。为了确定哪些文件包含查询中的所有词，您从查询中第一个词的倒排文件开始。然后，您依次考虑您已有的倒排文件与查询中每个后续词关联的倒排文件的交集（即公共元素）。当您以这种方式处理完查询中的所有词后，您剩下的倒排文件应该只包含包含查询中所有词的文件。

To make things more concrete, if you were to build an index on the small dataset, your search function should return the respective results shown in the seven examples below. (Again, note that the examples below are produced on a Mac, where file paths use: /. On a PC, you would see \
为了更具体起见，如果你在小数据集上构建索引，你的搜索功能应该返回下面七个示例中分别显示的结果。（再次注意，下面示例是在 Mac 上生成的，其中文件路径使用：/。在 PC 上，你会看到\
in the file paths instead).
在文件路径中（而不是）。

Example 1. Calling: search(index, 'apple')
Should produce the list: ['small/1.txt', 'small/2.txt', 'small/3.txt']

Example 2. Calling: search(index, 'ball')
Should produce the list: ['small/1.txt', 'small/3.txt']

Example 3. Calling: search(index, 'lizard')
Should produce the list: ['small/3.txt']

Example 4. Calling: search(index, 'apple ball')
Should produce the list: ['small/1.txt', 'small/3.txt']

Example 5. Calling: search(index, 'dog ball')
Should produce the list: ['small/1.txt']

Example 6. Calling: search(index, 'dog ball hamster')
Should produce the list: []

Example 7. Calling: search(index, 'nope')
Should produce the list: []
Doctests for the search function are provided for you. Feel free to write additional doctests. Also, you should definitely write additional functions that may help you decompose your solution to this problem.
为搜索函数提供的 doctests。您可以自由编写额外的 doctests。此外，您应该绝对编写一些额外的函数，这些函数可能有助于您分解这个问题的解决方案。

Running your search function
运行您的搜索功能
You can run your search function by running the searchengine.py program, specifying the directory name for a set of text files that you would like to index, and then add -s at the end of the command line to indicate "search mode". For example, you can run your program in "search mode" with the small dataset in a Python Terminal using this command (on the Mac, use python3 instead of py):
您可以通过运行 searchengine.py 程序来运行您的搜索功能，指定要索引的一组文本文件的目录名称，然后在命令行末尾添加 -s 来指示“搜索模式”。例如，您可以使用以下命令在 Python 终端中用小型数据集以“搜索模式”运行您的程序（在 Mac 上，请使用 python3 而不是 py）：

> py searchengine.py small -s
In search mode, the program will first build an index (and a file_title dictionary) on the files in the directory you specify by calling your create_index function. It will then repeatedly ask the user (you) for a query, which is sent (along with the index) to your search function to produce a posting list of results. These results are then displayed on the terminal, where, for each result, the title of the article and the associated file name are listed (making use of the file_title dictionary produced by your create_index function). You can end the program by simply pressing Enter when asked for a query (i.e., giving the empy query).
在搜索模式下，程序将首先在您指定的目录中的文件上构建一个索引（以及一个 file_title 字典），通过调用您的 create_index 函数。然后，它将反复要求用户（您）输入一个查询，该查询将与索引一起发送到您的 search 函数以生成结果列表。这些结果将在终端上显示，其中，对于每个结果，都会列出文章的标题和相关的文件名（利用由您的 create_index 函数生成的 file_title 字典）。当要求输入查询时，您可以通过简单地按 Enter 键来结束程序（即，提供一个空查询）。

Test your program thoroughly with the small dataset. That dataset is small enough that you can check your results manually to make sure that you are producing the expected output for various queries. You can also free free to create your own datasets (directories containing text files) to test out any particular cases you want to create to debug your code.
用小型数据集彻底测试你的程序。这个数据集足够小，你可以手动检查你的结果，以确保你针对各种查询产生了预期的输出。你也可以自由地创建自己的数据集（包含文本文件的目录），以测试你想要创建的任何特定案例来调试你的代码。

When you've think you've gotten your program working with the small dataset, try running your program with the BBC News data as follows:
当你认为你的程序在小数据集上已经可以运行时，请尝试按照以下方式使用 BBC News 数据运行你的程序：

> py searchengine.py bbcnews -s
Here is the output of a working program running on some sample queries on the BBC News data (user input is in blue italics). You can see if your program produces the same output. (Note that the order of the articles printed might be different depending on how you wrote your code, but the set of articles that match each query should be the same as in this sample run.)
以下是某个工作程序在 BBC News 数据集上针对一些示例查询的输出结果（用户输入以蓝色斜体显示）。你可以检查你的程序是否产生了相同的输出。（注意：打印文章的顺序可能会因你编写的代码不同而有所差异，但与每个查询匹配的文章集合应与这个示例运行结果相同。）

Query (empty query to stop): stanford
Results for query 'stanford':
1.  Title: Yahoo celebrates a decade online,  File: bbcnews/066.txt
2.  Title: Google to scan famous libraries,  File: bbcnews/217.txt
Query (empty query to stop): bike
Results for query 'bike':
1.  Title: Games help you 'learn and play',  File: bbcnews/291.txt
2.  Title: The Force is strong in Battlefront,  File: bbcnews/339.txt
Query (empty query to stop): stanford bike
Results for query 'stanford bike':
No results match that query.
Query (empty query to stop): windows virus security patch
Results for query 'windows virus security patch':
1.  Title: Microsoft releases patches,  File: bbcnews/003.txt
2.  Title: Microsoft releases bumper patches,  File: bbcnews/162.txt
Query (empty query to stop): cheap apple products
Results for query 'cheap apple products':
1.  Title: Apple Mac mini gets warm welcome,  File: bbcnews/033.txt
Query (empty query to stop): *user presses "enter" to end program*
Congratulations! You just built a working search engine! That's pretty impressive given that you might not have known a lot about programming just 10 weeks ago. It's also a testament to how powerful a tool programming can be. A little knowledge can go a long way in building some really useful software. Happy searching! The rest of the assignment is optional – though we think it's a great deal of fun + learning.
恭喜！你刚刚构建了一个可用的搜索引擎！考虑到你仅仅 10 周前可能对编程知之甚少，这确实令人印象深刻。这也证明了编程作为一个工具的强大之处。一点知识就能走很长的路，构建出一些非常有用的软件。祝你搜索愉快！剩下的作业是可选的——尽管我们认为它充满了乐趣和学习的价值。

[Optional] WebApp Extension: Your search engine online!
[可选] WebApp 扩展：您的在线搜索引擎！
As a celebration of what you have built, and as an exciting extension, let's turn your python program into a server which can deliver those search results to a web-appication, running as a website in a browser. Woot! This extension will give you exposure to some really interesting next steps beyond CS106A as well as practice with classes. It is optional meaning you don't need to complete it to finish what is expected for this assignment.
作为对您所构建内容的庆祝，以及一个令人兴奋的扩展，让我们将您的 python 程序转变为一个服务器，它可以将这些搜索结果交付到一个运行在浏览器中的 Web 应用程序。太棒了！这个扩展将使您接触到 CS106A 之外的一些真正有趣的下一步，以及练习使用类。它是可选的，这意味着您不需要完成它就可以完成此作业的预期要求。

Write code in extension_server.py that responds to search requests! In order to do so, link up your server to call the functions you defined in searchengine.py. If you run the starter code for extension_server.py it will create a server which can serve up the shell search page, but is unable to do any search. To get started run the server:
在 extension_server.py 中编写代码以响应用户搜索请求！为此，需要将服务器链接到调用 searchengine.py 中定义的函数。如果运行 extension_server.py 的启动代码，它将创建一个可以提供 shell 搜索页面的服务器，但无法执行任何搜索。要开始使用，请运行服务器：

> py extension_server.py
And navigate to http://localhost:8000 in a web-browser (such as Chrome, Safari or IE). How exciting. The starter code creates a bare-bones server which serves up the HTML of the search page, but does nothing more. HTML is the "markup language" of the world wide web – it's the description of the page with the search bar etc. When you try and search, this website sends a request to your server. In the starter code, your server does not respond to the query request so the web application does not work!
并在网络浏览器（如 Chrome、Safari 或 IE）中导航到 http://localhost:8000。太令人兴奋了。启动代码创建了一个基础的服务器，该服务器提供搜索页面的 HTML，但除此之外什么也不做。HTML 是“标记语言”，它是包含搜索栏等内容的页面描述。当你尝试搜索时，这个网站会向你的服务器发送请求。在启动代码中，你的服务器不会响应查询请求，因此 Web 应用程序无法工作！

If you look at the terminal where your server is running you will notice that every time someone types something into the search bar and hits "enter", you get a request. For example, say someone types in "nice" (as shown below):
如果你查看你的服务器正在运行的终端，你会注意到每次有人输入一些内容到搜索栏并按下"回车"，你就会收到一个请求。例如，假设有人输入了"nice"（如下所示）：

{style="width: min(100%, 500px)"}

The client (aka webpage) sends a request, which is received by your server, with the command "search" and parameters that include the search query. The server currently prints the request out to the console (as shown below), but doesn't handle it.
客户端（即网页）发送一个请求，该请求被您的服务器接收，其中包含命令"search"和包括搜索查询的参数。服务器目前将请求打印到控制台（如下所示），但没有处理它。

{'command': 'search', 'params': {'query': 'nice'}}
You can directly recreate this request by going to http://localhost:8000/search?query=nice
您可以直接通过访问 http://localhost:8000/search?query=nice 来重新创建此请求

Currently your server responds with the empty string. To complete this milestone, change the code to return a list of dictionaries, one dictionary per search result, with the key "title" and the value being the text of the title to display.
当前您的服务器响应为空字符串。要完成此里程碑，请更改代码以返回一个字典列表，每个搜索结果一个字典，其中键为"title"，值为要显示的标题文本。

{style="width: min(100%, 500px)"}

That is all you need to do! Once you do so, your search engine at http://localhost:8000 will start working as expected. How fun! It's a hard task as it requires writing code in a class which is a brand new experience.
那就是你需要做的全部！一旦你完成这些，你位于 http://localhost:8000 的搜索引擎将按预期开始工作。多有趣啊！这是一个艰巨的任务，因为它需要在类中编写代码，这是一次全新的体验。

Here are a few hints:
这里有一些提示：

Check out the HitCounter example from class on May 23rd.
查看 5 月 23 日课上讲的 HitCounter 示例。
Recall that request has two properties, commands and parameters. You can extract the command with request.get_command() and the parameter dictionary using request.get_params()
记住请求有两个属性，命令和参数。你可以用 request.get_command()提取命令，用 request.get_params()获取参数字典。
Your handle_request function has to return the list of dictionaries as a string. You can use json.dumps(collection, indent=2) to turn any collection (e.g. a variable that is a list or dictionary) into string format.
你的 handle_request 函数必须将字典列表作为字符串返回。你可以使用 json.dumps(collection, indent=2)将任何集合（例如一个列表或字典的变量）转换为字符串格式。
extension_server.py already imports the following functions from searchengine.py: create_index, search and textfiles_in_dir. You should call these functions! When do you want to create the index? When do you want to search?
extension_server.py 已经从 searchengine.py 中导入了以下函数：create_index、search 和 textfiles_in_dir。你应该调用这些函数！你想什么时候创建索引？你想什么时候搜索？
If you want your search engine to display more than just the title of an article, try adding "url" and "snippet" to the dictionary representing one search result. The WebApp is programmed to display these specific fields. These are extra extensions.
如果你想让你的搜索引擎不仅显示文章的标题，可以尝试在表示一个搜索结果的字典中添加"url"和"snippet"。WebApp 被编程为显示这些特定字段。这些都是额外的扩展。
How did we write that WebApp website? In this assignment we provide the website which is able to call your python code. Writing a website is a neat skill, which is certainly within your grasp to learn now that you have finished CS106A. It is certainly not necessary, but we invite you to read the contents of extension_client.html . This file describes the webpage you see (with the search bar). It is commented so that a curious student could learn more about HTML, JavaScript and CSS. Those aren't things we teach in CS106A, but they are super cool!
我们是如何编写那个 WebApp 网站的？在这个作业中我们提供了能够调用你的 python 代码的网站。编写网站是一项很棒的技能，现在你已经完成了 CS106A，这一定在你的掌握之中。当然不是必须的，但我们邀请你阅读 extension_client.html 的内容。这个文件描述了你看到的网页（带有搜索栏）。它有注释，以便好奇的学生可以了解更多关于 HTML、JavaScript 和 CSS。这些不是我们在 CS106A 教授的内容，但它们超级酷！

A note on localhost: Localhost is a special URL which means the website being served from "this computer". People on different computers won't be able to access your python script over the internet using the localhost URL. To get a URL which other people can use, you can use a service like the one here: https://ngrok.com/
关于 localhost 的说明：Localhost 是一个特殊 URL，表示网站从“这台计算机”提供服务。不同计算机上的人无法使用 localhost URL 通过互联网访问你的 python 脚本。要获取其他人可以使用的 URL，你可以使用类似这里的工具：https://ngrok.com/

[Optional] Other Extension Features
[可选] 其他扩展功能
There are many other possibilities for optional extra features that you can add if you like, potentially for extra credit. If you are going to do this, please submit two versions of your program: one that meets all the assignment requirements, and a second extended version. As usual, in the Assignment 7 project folder, we have provided a file called extension.py that you can use if you want to write any extensions that you might want to make based on this assignment. The file doesn't contain any useful code to begin with. So, you only need to submit the extension.py file if you've written some sort of extension in that file that you'd like us to see.
如果你喜欢，还有许多其他可选的附加功能可以添加，这可能有助于获得额外加分。如果你打算这样做，请提交你的程序的两个版本：一个满足所有作业要求，另一个是扩展版本。和往常一样，在 Assignment 7 项目文件夹中，我们提供了一个名为 extension.py 的文件，如果你想要基于这个作业编写任何扩展，可以使用它。这个文件一开始不包含任何有用的代码。因此，只有当你在这个文件中编写了某种扩展并希望我们查看时，才需要提交 extension.py 文件。

At the top of the files for an extended version (if you submit one), in your comment header, you should comment what extra features you completed.
在扩展版本文件（如果你提交的话）的顶部，在你的注释头部，你应该注释你完成了哪些额外功能。

Here are a few extra extension ideas:
这里有一些额外的扩展想法：

Ranking function. The basic search program just lists all the documents that match the query in no particular order. It would be much more useful, especially with large collections of documents, if the documents were ranked (sorted) by their relevance to the user's query. We talked about some ways to do this in class, but there are many different approaches to this. Try implementing a ranking function that you think does a good job of ordering the search results. As we talked about, that might involve augmenting your index to store more information than just which terms appeared in which documents, so you can use that information to determine how to rank the search results.
排名函数。基本的搜索程序只是按无特定顺序列出所有与查询匹配的文档。如果文档按其与用户查询的相关性进行排名（排序），则将更有用，尤其是在处理大量文档时。我们在课堂上讨论了一些方法，但这种方法有很多不同的途径。尝试实现一个你认为能很好地对搜索结果进行排序的排名函数。正如我们讨论的，这可能涉及增强你的索引以存储比仅哪些术语出现在哪些文档中更多的信息，以便你可以使用这些信息来确定如何对搜索结果进行排名。
Stop word elimination. The English language has many words that appear frequently in text, but don't have much value as far as content is concerned. These are words such as "the", "and", "but", "a", etc. Such words are called stop words, and it would make your index smaller if you removed the stop words from the index. (That also means you'd potentially want to remove stop words from the user's query before doing a search.) Of course, you can find out more about stop words (as well as find potential lists of them) by searching the web for "stop words".
停止词消除。英语中有许多词在文本中频繁出现，但就内容而言价值不大。这些词包括“the”、“and”、“but”、“a”等。这些词被称为停止词，如果你从索引中删除停止词，可以使索引更小。（这也意味着在执行搜索之前，你可能想要从用户的查询中删除停止词。）当然，你可以通过在网络上搜索“停止词”来了解更多关于停止词的信息（以及找到潜在的停止词列表）。
Word stemming. In your current index, if a user searches for "section" they won't match files that contain the word "sections" (but don't include the singular form of the word "section"), even though files that talk about "sections" might be relevant to the user. Stemming is the process of reducing words to their base form, so that (for example) both "section" and "sections" would become, simply, "section". Word stemming is a common feature in commercial search engines as it's very useful for helping people get relevant results. As a start, you can find out more about word stemming from Wikipedia: https://en.wikipedia.org/wiki/Stemming
词干提取。在您当前的索引中，如果用户搜索"section"，他们不会匹配包含单词"sections"的文件（但不包括单词"section"的复数形式），尽管谈论"sections"的文件可能对用户相关。词干提取是将单词减少到其基本形式的过程，因此（例如）"section"和"sections"都会简单地变成"section"。词干提取是商业搜索引擎中的一个常见功能，因为它对于帮助人们获得相关结果非常有用。作为开始，您可以从维基百科了解更多关于词干提取的信息：https://en.wikipedia.org/wiki/Stemming
Ethics Questions  伦理问题
Although Sergey Brin and Larry Page didn't take CS106A with embedded ethics at Stanford, they also considered questions about the ethics of search as they developed their search engine. Below is an excerpt from their paper describing the PageRank algorithm that became the core of the Google search engine. We ask you to read this excerpt and then reflect on the contents, framing your analysis in the context of the ehtics portion of Monday's lecture (May 23rd).
尽管 Sergey Brin 和 Larry Page 没有在斯坦福大学选修 CS106A 嵌入伦理课程，但在开发他们的搜索引擎时，他们也考虑了关于搜索伦理的问题。以下是他们描述成为谷歌搜索引擎核心的 PageRank 算法的论文摘录。我们要求你阅读这篇摘录，然后反思内容，并将其分析置于周一讲座（5 月 23 日）的伦理部分背景下。

"Currently, the predominant business model for commercial search engines is advertising. The goals of the advertising business model do not always correspond to providing quality search to users. [...] For this type of reason and historical experience with other media [Bagdikian 83], we expect that advertising funded search engines will be inherently biased towards the advertisers and away from the needs of the consumers.
目前，商业搜索引擎的主要商业模式是广告。广告商业模式的目標并不总是与为用户提供高质量搜索服务相一致。[...]由于这类原因以及与其他媒体的历史经验[ Bagdikian 83]，我们预计，由广告资助的搜索引擎将天生倾向于广告商，而忽视消费者的需求。

Since it is very difficult even for experts to evaluate search engines, search engine bias is particularly insidious. [...] This type of bias is much more insidious than advertising, because it is not clear who "deserves" to be [at the top of search results], and who is willing to pay money to be listed. [...] But less blatant bias [sic] are likely to be tolerated by the market. For example, a search engine could add a small factor to search results from "friendly" companies, and subtract a factor from results from competitors. This type of bias is very difficult to detect but could still have a significant effect on the market. [...] [W]e believe the issue of advertising causes enough mixed incentives that it is crucial to have a competitive search engine that is transparent and in the academic realm."
既然即使是专家也很难评估搜索引擎，搜索引擎的偏见就特别隐蔽。 [...] 这种偏见比广告更隐蔽，因为不清楚谁“应该”出现在搜索结果的顶部，以及谁愿意付钱来获得排名。 [...] 但市场可能更容易容忍不太明显的偏见。[sic] 例如，搜索引擎可能会给来自“友好”公司的搜索结果增加一个小的因素，而给竞争对手的结果减去一个因素。这种偏见很难检测，但仍然可能对市场产生重大影响。 [...] [W]我们相信广告问题已经造成了足够复杂的动机，因此需要一个透明且处于学术领域的竞争性搜索引擎。

Question 1 Brin and Page were worried that search companies that were paid by advertisers would be inclined to modify their ranking of results to give more favorable treatment to those advertisers? Do you believe this is a concern and if so, what approach (at a high-level) might you suggest to address it?
问题 1：布林和佩奇担心那些由广告商付费的搜索引擎公司可能会倾向于修改其搜索结果排名，以给予这些广告商更优惠的待遇吗？你认为这是一个问题吗？如果是，你建议采取什么（高层次的）方法来解决它？

Question 2 In this excerpt, Brin and Page express concerns about the negative impacts of advertising on search engine quality and results. Their main observation is that monetary incentives are likely to bias search engine results such that they are less likely to provide the most relevant content to the searcher. Bias towards advertisers is not the only potential problem with search results, however. Based on our discussion in lecture, how might you address these problems? How could you alter or extend your Bajillion search engine to deliver multiple perspectives to the same searcher? To deliver personalized results? To be more transparent about why it delivers the results it does? Which of these goals is most important and why?
问题 2 在这段摘录中，布林和佩奇对广告对搜索引擎质量和结果产生的负面影响表示担忧。他们的主要观察是，经济激励可能会使搜索引擎结果产生偏差，从而不太可能向搜索者提供最相关的内容。然而，对广告商的偏见并不是搜索结果潜在问题的唯一来源。根据我们在讲座中的讨论，你如何解决这些问题？你如何修改或扩展你的 Bajillion 搜索引擎，以向同一搜索者提供多个视角？如何提供个性化结果？如何更加透明地说明它为什么提供这些结果？在这些目标中，哪个最重要，为什么？

Like in previous assignments, please write your answers in ethics.txt
如同之前的作业一样，请将你的答案写在 ethics.txt 中

Submitting your work  提交你的作品
Once you've gotten all the parts of this assignment working, you're ready to submit! Make sure to submit only the python files you modified for this assignment on Paperless. You should make sure to (at least) submit the files:
一旦你完成这个作业的所有部分，就准备好提交了！确保在 Paperless 上只提交你为这个作业修改的 Python 文件。你应该确保（至少）提交以下文件：

common_elements.py
searchengine.py
ethics.txt
Credit  信贷
[1]: The BBC News dataset is a collection of articles covering technology news. We reference the paper which was responsible for making this dataset available to the research community: D. Greene and P. Cunningham. "Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering", Proc. ICML 2006. Please note that all rights, including copyright, in the content of the original articles are owned by the BBC. The articles are used here only for educational purposes.
[1]: BBC News 数据集是一个涵盖科技新闻的文章集合。我们参考了负责将此数据集提供给研究社区的论文：D. Greene 和 P. Cunningham。 "解决核文档聚类中对角占优问题的实用方案"，ICML 2006 会议论文集。请注意，原始文章内容的所有权利，包括版权，均归 BBC 所有。这些文章仅用于教育目的。

Ethics questions written by Kathleen Creel, Nick Bowman, and Mehran Sahami.
由 Kathleen Creel、Nick Bowman 和 Mehran Sahami 撰写的伦理问题。

Warmup: Finding common elements in two lists
热身：在两个列表中查找公共元素
The Bajillion Search Engine
Bajillion 搜索引擎


[Optional] WebApp Extension: Your search engine online!
[可选] WebApp 扩展：您的在线搜索引擎！
[Optional] Other Extension Features
[可选] 其他扩展功能
Ethics Questions  伦理问题
Submitting your work  提交你的工作
Credit  信用
All course materials © Stanford University 2021
所有课程材料 ©斯坦福大学 2021
Website programming by Julie Zelenski • Styles adapted from Chris Piech • This page last updated 2022-May-23
网站编程由 Julie Zelenski 完成 • 样式改编自 Chris Piech • 本页面最后更新于 2022 年 5 月 23 日