Tell me about a time when you had to re-think your approach on a project because you received new information

Situation:
During my internship as an ML Intern at Shopify, I was working on a fast-paced team focused on improving product recommendations. I was tasked with developing a diversifier based on the MMR (Maximal Marginal Relevance) algorithm to enhance the diversity of product listings.

Task:
My goal was to implement the post-processing component of the diversifier, run evaluations, and present performance data to inform the team’s iteration process. However, as I was preparing my initial results, the composite model I was evaluating against was updated, requiring a re-run of all evaluations using the new version.

Action:
I re-ran the evaluations with the updated composite version, but encountered an issue: no products were being loaded during the evaluation step. There were no helpful logs in the terminal, so I manually queried BigQuery using the run ID and confirmed that data existed. When I ran the pipeline manually, it worked—but the script that triggered the evaluation DAG consistently failed.
To investigate further, I consulted with a more senior engineer and learned about a DAG monitoring tool I hadn’t used before. Using that tool, I discovered that a new validation check had been recently added to the DAG, and my code didn’t meet that requirement. I referenced where the new check had been implemented in the codebase, made the necessary changes to my own code, and successfully reran the evaluations.

Result:
I was able to complete the updated evaluations and present the results in time for the team to use in the next iteration. More importantly, I learned the importance of staying aligned with ongoing changes in a highly collaborative and fast-moving environment. This experience shifted my mindset from working in a silo to proactively seeking context in others' contributions and treating my work as part of a larger, interconnected system.