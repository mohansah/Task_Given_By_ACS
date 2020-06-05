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
