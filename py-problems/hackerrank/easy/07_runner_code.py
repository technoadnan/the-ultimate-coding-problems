if __name__ == '__main__':
   n = int(input())
   arr = list(map(int, input().split()))
   
   # Convert the list to a set to remove duplicates, then convert back to a sorted list
   unique_scores = sorted(set(arr), reverse=True)
   
   # The runner-up score will be the second highest unique score
   if len(unique_scores) > 1:
      runner_up_score = unique_scores[1]
   else:
      runner_up_score = unique_scores[0]
   
   print(runner_up_score)
