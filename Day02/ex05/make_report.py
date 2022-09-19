##!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python
import config
import analytics as al


def main():
    research = al.Research(config.DATA_FILE_NAME)
    try:
        res = research.file_reader(has_header=config.DATA_HAS_HEADER)
    except Exception as e:
        print(type(e).__name__, e, sep=': ')
        return

    calc = research.Analytics(res)
    count = calc.counts()
    fraction = calc.fractions(count)
    predict_rand = calc.predict_random(config.NUM_OF_STEPS)
    report = config.REPORT_TEXT.format(sum(count), count[0], count[1],
                                       round(float(fraction[0]), 2), round(float(fraction[1]), 2), config.NUM_OF_STEPS,
                                       predict_rand.count(['0', '1']),
                                       predict_rand.count(['1', '0']))
    calc.save_file(report, 'report', "txt")


if __name__ == '__main__':
    main()