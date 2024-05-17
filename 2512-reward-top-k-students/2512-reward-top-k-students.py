class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]: 

        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        res = {}
        
        feedback = [each.split() for each in report]

        print(feedback)

        for feed, stud in zip(feedback, student_id):
            mark = 0
            for val in feed:
                if val in positive_feedback:
                    mark += 3
                elif val in negative_feedback:
                    mark -= 1

            res[stud] = mark

        res = sorted(res.items(), key=lambda item: (-item[1], item[0]))
        
        # Extract the top k student IDs
        return [student[0] for student in res[:k]]
        
        # return top_students