# Perl version.
# sub pairwise_sum {
#     my($arg1, $arg2) = @_;
# my @result;
# for(0 .. $#$arg1) {
# push(@result, $arg1->[$_] + $arg2->[$_]);
# }
# return(\@result);
# }


# Python version.
def pairwise_sum(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result


print("Hellow World")

if __name__ == "__main__":
    print("Hellow world")
