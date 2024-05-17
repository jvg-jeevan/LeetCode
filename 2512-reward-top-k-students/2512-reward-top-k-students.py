class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]: 

# remove the duplicates from positive and negative_feedback
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

# res dict() key= student_id, value= mark(based on pos and neg feedbacks)
        res = {}
        
# feedback stores list of each string
        feedback = [each.split() for each in report]

        print(feedback)

# for each feedback and student_id
        for feed, stud in zip(feedback, student_id):
# mark to count the number of positive and negaticve feedbaks
            mark = 0
            for val in feed:
# for each val in feedback of indivisual count the number of pos and neg feedback
                if val in positive_feedback:
                    mark += 3
                elif val in negative_feedback:
                    mark -= 1

# res dict() for every student mark of pos and neg
            res[stud] = mark

# sort the dict based on increasing order of student id and decreasing order of mark(pos - neg)
        res = dict(sorted(res.items(), key=lambda item: (-item[1], item[0])))
        print(res)
        
# return the top k student_id (key)
        return list(res.keys())[:k]