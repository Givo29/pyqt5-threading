# PyQT5 Threading The Right Way

### History
After researching PyQT5 threading while updating a simple app with [cleary](https://github.com/cleary), we found that most of the documentation regarding this topic is incorrect, including official documentation.

We eventually stumbled across a few articles (listed below) that had correct methods and documentation as to how this works.

**Reference:** 
 * https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/  
 * https://stackoverflow.com/questions/11426335/qthread-execution-freezes-my-gui
 * https://blog.qt.io/blog/2010/06/17/youre-doing-it-wrong/ ...which dead links to where they promise the real information is. [Here is the referenced blog post on archive.org](https://web.archive.org/web/20200128030120/https://www.qt.io/blog/2006/12/04/threading-without-the-headache)

### Example Code:

Functional threading example: [main.py](https://github.com/Givo29/pyqt5-threading/blob/master/main.py)
