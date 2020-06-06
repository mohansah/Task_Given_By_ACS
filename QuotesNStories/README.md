# Problem Statement

Suppose you are given with 50,000 company websites and a short description of the companies like below.  You need to build out a recommendation platform such as for a given company you need to find similar companies based on the description of the company.

#### For example :- 

1. Gitlab.com => “From project planning and source code management to CI/CD and monitoring, GitLab is a complete DevOps platform, delivered as a single application. Only GitLab enables Concurrent DevOps to make the software lifecycle 200% faster.”
2. Cloudbees.com => “Reduce risk, optimize software delivery and accelerate innovation with CloudBees - the industry-leading DevOps technology platform. Build Stuff That Matters.”
3. squarespace..com => “Squarespace is the all-in-one solution for anyone looking to create a beautiful website. Domains, eCommerce, hosting, galleries, analytics, and 24/7 support all included."
4. Wix.com => “Create a free website with Wix.com. Choose a stunning template and customize anything with the Wix website builder—no coding skills needed. Create yours today!”


#### In the above example
1. For a given input Gitlab.com => it should return Cloudbees.com and viceversa. 
2. Similarly for an input wix.com => it should return squarespace.com





# Solution
### About Dataset
From the docs you shared, I used that info & created a CSV file (SimilarCompaniesRecommendation.csv) which contains two columns. First column contains description of the company and second column contains company website.

### About Code
I wrote two type of code:

Code1: Similar Companies Recommendation Code 1, where we have only one input parameter which is company website.
	In this case the description of the input company website must be present in the dataset.

Code 2: Similar Companies Recommendation Code 2, where we have two input parameters which are company website and company description.
	In this case the description of the input company website may or may not be present in the dataset.

I have created three functions in both the code:
1.	Function “description_cleaning()”
Purpose: To clean the description of companies i.e., data cleaning
2.	Function “find_similarity()”
Purpose: To find similarity between two description using cosine similarity
3.	Function “find_similar_company()”
Purpose: To find similar company to the input company website

Function 1 and 2 are called under the Function 3 so Function 3 are my main function and I used this function to print the results.

### Approached Method
1.	Data Reading
2.	Data Cleaning
3.	Calculating cosine similarity values between description of input company website and rest of the website.
4.	Sort the data on the basis of cosine similarity values and assigned the rank, i.e., Lower the rank higher the similarity value means Rank 1 is most similar to the input company and as rank increases similarity decreases.
5.	Printing the Similar Companies website with Rank.
