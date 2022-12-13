# Deanonymizing-Datasets
This week, there are two tasks, one synthesis and one exploration. Task 1 involves a fair bit of coding. As usual, we can provide the most help for a Python 3 solution, but ultimately you're welcome to work in whatever language you are most comfortable with.

Task 1: Synthesis: Deanonymization (75 points)
This task consists of four sections. In this task, you will read a file released by Last.fm Links to an external site.of pseudonymous users and which musical artists they listened to (and how many times). The Last.fm dataset was released by researchers Links to an external site.in the field of information retrieval.

You will use a variant of the main technique used in the Narayanan and Shmatikov paper Links to an external site.we referenced in class to deanonymize this dataset by matching the pseudonymous user IDs in the Last.fm dataset with the names on a non-anonymous music website https://computersecurityclass.com/ Links to an external site.(a domain Blase saw was available a few years ago and decided to buy). Imagine that computer security fans are now running a music website.

Before you start coding, read Sections 1, 3, and 4 of the Narayanan and Shmatikov paper Links to an external site.. This will help you a lot in approaching the task in a sensible way!

1.1: Read the Last.fm files (3 points)
Download the file lastfmhetrec2011-lastfm-2k.zip that we have provided. Unzip it and peruse the readme.txt file to understand the structure and semantics of the data it provides. For this assignment, you will only need the data from user_artists.dat (containing the artists a user has listened to, as well as how many times) and artists.dat (which is a mapping from the artist ID numbers in the previous file to the artists' names).

(2 points) Your first task is simply to read those files and process them into a format that will be useful for the way you approach the subsequent exercises. You'll probably want to read the rest of the assignment first to determine what format that might be.

Write-up Question 1 (1 point): Briefly explain why you chose the data representations you did.

1.2: Scrape data from the web (25 points)
Recall that there is a non-anonymous music website at https://computersecurityclass.com/ Links to an external site.that has people's first names and their listening habit in a slightly different format than the Last.fm file. In this step, you'll need to get that data into a format that will allow you to compare with the Last.fm data from the previous step. Be aware that there are some subtle, yet important, differences between the data formats.

(20 points) Figure out the format in which you'll want to store this data. Then go ahead, scrape those webpages, extract the data you need, and store it in your chosen format.

How do you download webpages in Python? Look up the urllib.request library for Python3 Links to an external site., though note that you'll probably want to find a more compact tutorial for how to use it effectively for this task. (Don't be confused by other tutorials you find referencing things like urllib2 -- that was for the old version of Python, Python 2.)

How do you extract the data you need from the page? If you want to do this by hand, you'll want to use regular expressions, which are a way in most programming languages of defining patterns and then matching those patterns in text you have. The w3schools Links to an external site.and programiz Links to an external site.both have short tutorials that are a good starting place, though you might want to look up other tutorials as well. However, if you want to do this partially automatically, read about the Beautiful Soup Links to an external site.library, which we highly recommend.

Once you read in the contents a particular webpage and extract the important information, you're ready to put it in your data structure.

Write-up Question 2 (5 points): Briefly explain the steps you had to take to extract the data (3 points) and get it into an appropriate format for comparing with the Last.fm data (2 points).

1.3: Define a similarity function for pairs of records (10 points)
On page 3 of the Narayanan and Shmatikov paper Links to an external site., they define a metric called Sim that takes two "records" as input and defines their similarity based essentially on the cosine similarity Links to an external site., which is explained a bit more practically on https://www.machinelearningplus.com/nlp/cosine-similarity/ Links to an external site.. In the latter link, pay particular attention to the "Cosine Similarity Formula."

(10 points) Turn the data you collected in the previous two problems into a format suitable for this task and then define a function for computing Sim given two records. We don't require any explicit code output or explanation, just the code defining your Sim function.

Hint 1: we recommend having the input "records" be vectors (Python lists) of size N, where N is the number of unique artists seen in either data set. The N'th element of the vector will be how many times a person listened to the N'th artist according to the data set represented by that record.

Hint 2: I (Blase) think the paper is kind of vague about the definition of Sim. My overall hope is for you all to think about the possible definitions here and choose an approach you're comfortable with. That said, I figured I'd outline a few different approaches you can take. There's not necessarily one right one; each has different pros and cons.

One option is to ignore exactly what the authors proposed for Sim and instead just go ahead and calculate cosine similarity. Note that you don't need to try to fit cosine similarity into the definition of the similarity function. Instead, just replace the whole formula with cosine similarity. This isn't the best approach, though. This Stack Overflow post Links to an external site.has some good examples of how to calculate cosine similarity both using and not using well-known libraries. Kind of hilariously, the original question answer was trying to get Stack Overflow to do their homework for them. You'll need to think, though, what is the right data representation if you want to use any of these built-in libraries. Making a list the size of the number of artists in the datasets for each user is going to take a fair bit of RAM. Is there any way you can avoid redundant computation or writing a bunch of 0's to memory? I'm sure you can calculate cosine similarity in a much, much more efficient way for your (sparse) dataset if you think through which terms will be zeroes (and thus can be dropped), as well as what computation you can do once and then cache. In my sample solutions, I just implemented cosine similarity somewhat manually. If you're using cosine similarity, think carefully about whether you want to use the absolute number of listens or if you want to normalize the listens for each person.

If you instead want to follow the paper's definition more closely, and this is very reasonable and something we'd encourage, let's clarify what some of the terms mean. Being a bit backwards, let's start with the denominator. The paper writes, "For example, the shopping history of even the most profligate Amazon shopper contains only a tiny fraction of all available items. We call these attributes non-null; the set of non-null attributes is the support of a record (denoted supp(r))... The support of a column is defined analogously." So the denominator ends up being just a count of how many artists were listened to by Person 1 (more formally Record 1, or r_1), Person 2 (more formally Record 2, or r_2), or both. So the size of the union of the artists listened to by either. For what it's worth, you don't get extra points for using the word "profligate" in a scientific paper; that's only on the SATs or GREs. The numerator is basically referring to how you compare the listens for the i'th artist in Record 1 and Record 2 and output 1 if they are "similar" in listens and 0 if they are "dissimilar." You're probably more familiar with "indicator function" referring to outputting 1 if something is a member of a set and 0 otherwise. So it's basically the sum of the number of artists for whom listens are similar between Person 1 and Person 2.

So this gets to the question of how you define "similar." Are you normalizing the listening counts for each person (record) and then comparing the distributions? If you're keeping it with raw numbers, are you looking for a particular number (e.g., the counts are within 3 listens of each other) or a percentage difference? As OP wonders, yes, you do have to decide what your threshold is for similarity. You'll also have to pick a threshold in most cases for Task 2.4.

What if Person 1 and Person 2 both listened to a particular artist 0 times. Is that similar or dissimilar, which is what OP sensibly asked? I agree that the paper is very vague about this. Think about this, though... is the knowledge that both people listened to some obscure Scandinavian death metal band equally as important in deanonymization as the knowledge that both people did not listen at all to some obscure Scandinavian death metal band? I'd argue no, so that should give you the intuition for what to report for similarity when both values are 0.

Of course, you could also perhaps improve on the authors' definition even more and report not just 1 or 0 for the similarity in each term in the numerator's summation, but maybe report a real value in the range [0, 1] indicating the similarity. You'll note that, in Section 4 of the paper, the authors introduce as one strategy weighting each term in the numerator inversely proportionally to the popularity of that artist. That is, inversely proportional to the "support" of that artist, which they define as the number of people (records) that have a non-null (i.e., non-zero) number of listens for that artist.

So, in short, you have a bunch of design decisions to make in your initial similarity function and then in adopting one of the many strategies they outline for deanonymization.

The authors tbh don't do a great job of rigorously evaluating the different strategies they propose, but the do introduce a lot of interesting ideas. That's why I decided to leave it up to all of you how to interpret what they're arguing and decide exactly how you wanted to apply it to deanonymizing this dataset. We'll grade you on whether you make sensible decisions in the different parts, and ultimately on how well you deanonymize the records.

1.4: Deanonymize (37 points)
Go ahead and compute Sim for every pair of records in which one record represents a user in the Last.fm dataset and the other record represents a user in the computersecurityclass.com dataset.

Write-up Question 3 (7 points): Section 4 of the Narayanan Narayanan and Shmatikov paper Links to an external site.presents multiple deanonymization approaches. Choose one of the approaches, which you'll implement in the rest of this task. In your write-up, briefly explain your approach in identifying matches, explaining how your approach is based on the paper.

(25 points) Using the approach you've decided upon, write code that decides (programmatically) which ID numbers from Last.fm correspond to which names from computersecurityclass.com. Note that not everyone in one dataset is in the other. You also won't necessarily find any 'exact' matches by your Sim metric. Write your code for the pairwise comparisons across the two datasets and deciding which user in one dataset matches to which user in the other dataset (or perhaps no one in the other dataset!).

(5 points) Output a JSON file mapping computersecurityclass.com names to Last.fm ID numbers. Users for whom there is not a match in the other dataset should be excluded from this JSON file. Example: {"Blase": "4", "Valerie": "100"}. The order does not matter. Save this file as matches.json and include it among the files you upload to Canvas.

Task 2: Exploration: Ethics of a Research Study (25 points)
This task will be our first engagement (to be continued in later assignments) on a controversy about the ethics of a computer security research study that was accepted for publication at a conference last year.

The paper in question, which you will only need to read parts of (see below), is:

Qiushi Wu and Kangjie Lu. On the Feasibility of Stealthily Introducing Vulnerabilities in Open-Source Software via Hypocrite Commits Links to an external site.. Originally accepted to Proc. IEEE S&P, 2021.
Read the abstract and Sections 1, 2, and 6 of the original paper. Feel free to skim (or skip) the rest. 

Then read both of the following articles about the start of the controversy around this paper last spring:

Steven J. Vaughan-Nichols. Greg Kroah-Hartman bans University of Minnesota from Linux development for deliberately buggy patches Links to an external site.. ZDNet, April 21, 2021.

Nathaniel Mott. University Responds to Ban On Linux Contributions Links to an external site.. Tom's Hardware, April 22, 2021.

Then read, in full, an explanation the authors released Links to an external site..

Write-up Question 4 (4 points): In your own words, succinctly state the key research question(s) the authors aimed to answer.

Write-up Question 5 (7 points): In your own words, describe the authors' methods in a paragraph or two.

Write-up Question 6 (7 points): What were the specific ethical issues raised in the way this study was conducted based on your own thoughts after reading the paper's methods, as well as what you read about the controversy?

Write-up Question 7 (7 points): Based just on this task, state in bullet points what you believe to be key, generalizable principles for what makes a research study ethical.
