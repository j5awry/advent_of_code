def main():
    with open("input.txt", "r") as fopen:
        sonar_readings = fopen.readlines()
        sonar_readings_nums = [int(x.strip()) for x in sonar_readings]
        increases = 0
        previous = sonar_readings_nums[0]
        for num in sonar_readings_nums[1:]:
            num = int(num)
            print(f"Previous: {previous} \n Current: {num}")
            if num > int(previous):
                increases += 1
                print(increases)
            previous = num
        print(increases)


if __name__ == "__main__":
    main()
