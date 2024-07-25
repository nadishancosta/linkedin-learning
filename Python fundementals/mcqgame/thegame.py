from Questions import Questions

qprompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

qobjs = [
    Questions(qprompts[0],"a"),
    Questions(qprompts[1],"c"),
    Questions(qprompts[2],"b")
    ]


def run_test(qobjs):
    answer=""
    correct=0
    for index in qobjs:
        answer=input(index.qs)
        if answer == index.ans.lower():
            correct += 1
        print("\n\n\n")
    return correct

print("Welcome to MCQS!!!\n")
testrun = run_test(qobjs)
print(f'\n\nYou got {testrun}/{len(qprompts)} questions right')