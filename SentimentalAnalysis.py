import Database as db
import Stats

class SentimentalAnalysis:
    def getNaiveBayesResult(self, msg, sts):
        np = pp = 1
        for m in msg.split(' '):
            if not self.isExactString(sts.stats, m):
                pp *= sts.getDefaultProbability("Pos")
                np *= sts.getDefaultProbability("Neg")
            elif self.isExactString(sts.stats, m):
                np *= sts.stats[m]["NegProb"]
                pp *= sts.stats[m]["PosProb"]
        if (pp > np):
            return "Positive"
        elif (pp<np):
            return "Negative"
        return "Neutral"

    def getBayesianBayesResult(self, msg, sts):
        np = pp = 1
        for m in msg.split(' '):
            if not self.isExactString(sts.stats, m):
                pp *= sts.getDefaultProbability("Pos")
                np *= sts.getDefaultProbability("Neg")
            elif self.isExactString(sts.stats, m):
                np *= sts.stats[m]["NegProb"]
                pp *= sts.stats[m]["PosProb"]
        np *= (sts.negCount / (sts.posCount + sts.negCount))
        pp *= (sts.posCount / (sts.posCount + sts.negCount))
        if (pp > np):
            return "Positive"
        elif (pp < np):
            return "Negative"
        return "Neutral"

    def isExactString(self, dict, st):
        for i in dict.keys():
            if i==st:
                return True
        return False


dataset=db.Database()
sts=Stats.Stats(dataset.unique_words)
sa=SentimentalAnalysis()
msg="films good best"

"""for i in msg.split():
    if i in sts.stats:
        print(i, sts.stats[i])"""
print(sts.posCount, sts.negCount, len(sts.stats))
print(sa.getNaiveBayesResult(msg, sts))
print(sa.getBayesianBayesResult(msg, sts))

print()