def convert_grade(score):
    assert 0 <= score <= 100, "成绩应在0-100之间"
    if score >= 90:
        return "A：优秀"
    elif score >= 80:
        return "B：良好"
    elif score >= 60:
        return "C：合格"
    else:
        return "D：及格"

# 输入两个学生的成绩
score1 = float(input("请输入第一个学生的成绩："))
score2 = float(input("请输入第二个学生的成绩："))

# 打印转换后的成绩等级
print("第一个学生的成绩等级为：", convert_grade(score1))
print("第二个学生的成绩等级为：", convert_grade(score2))