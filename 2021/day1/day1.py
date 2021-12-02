def compare_sequential(sonar_readings_nums):
    """
    Given a list of ints, compare each index against the previous index
    and count when the new index is higher than previous
    return: int
    """
    increases = 0
    previous = sonar_readings_nums[0]
    for num in sonar_readings_nums[1:]:
        num = int(num)
        print(f"Previous: {previous} \n Current: {num}")
        if num > int(previous):
            increases += 1
            print(increases)
        previous = num
    return increases


def compare_windowed(readings, window=3):
    """
    Given a list of ints, and optional window size
    compare added values from windows
    199  A      
    200  A B    
    208  A B C  
    210    B C D
    200  E   C D
    207  E F   D
    240  E F G  
    269    F G H
    260      G H
    263        H

    where the window is the Right columns:

    A: 607 (N/A - no previous sum)
    B: 618 (increased)
    C: 618 (no change)
    D: 617 (decreased)
    E: 647 (increased)
    F: 716 (increased)
    G: 769 (increased)
    H: 792 (increased)
    """
    increases = 0

    for index, value in enumerate(readings):
        previous = sum(readings[index:index+window])
        current = sum(readings[index+1:index+window+1])
        if current > previous:
            increases += 1
    return increases


def main():
    with open("input.txt", "r") as fopen:
        sonar_readings = fopen.readlines()
        sonar_readings_nums = [int(x.strip()) for x in sonar_readings]
        print(compare_sequential(sonar_readings_nums))
        print(compare_windowed(sonar_readings_nums))


if __name__ == "__main__":
    main()
