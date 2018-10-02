import twint

# Configure
c = twint.Config()
c.Search = "aurora shooting"
c.Since = "2012-07-20"
c.Until = "2012-07-28"
c.Output = "test.csv"
c.Format = "{tweet}"

# Run
twint.run.Search(c)
