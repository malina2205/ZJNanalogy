require 'optparse'
require 'ostruct'

  def parse(args)
    # The options specified on the command line will be collected in *options*.
    # We set default values here.
    options = OpenStruct.new
    options.skip_short = 0
    options.rand_dic = false


    opt_parser = OptionParser.new do |opts|
      opts.banner = "Usage: example.rb [options]"
      opts.separator ""
      opts.separator "Specific options:"


      # Optional argument; multi-line description.
      opts.on("-r", "--rand",
              "Losuj nowy slownik") do |ext|
        options.rand_dic = true
      end
      opts.on("-s N", Float,
              "Losuj nowy slownik") do |n|
        options.skip_short = n
      end
    end

    opt_parser.parse!(args)
    options
  end  # parse()
options = parse(ARGV)


lem_src = "tekst_lemma"
an_src = "tekst_analogy"

if options.rand_dic
    system('python randLexicon.py')
    system('python analogyAlgorithm.py -i tekst -f 1 -o tekst_analogy')
end

file_l = File.open(lem_src, "r")
file_a = File.open(an_src, "r")


tab_ana = []
tab_lem = []

File.open("tekst_lemma","r") do |master|
    master.each_line do |line|
        tab_lem << line.chomp
    end
end


File.open("tekst_analogy","r") do |query|
    query.each_line do |line|
        if !tab_lem.include? line.chomp
            tab_ana.push line.chomp.delete(' ').split("|")
        end
    end
end

n = tab_lem.length-1
tp = 0
fp = 0
all = 0
for i in 0..n
    if options.skip_short>0 and tab_lem[i].length <=options.skip_short
        next
    end
    if tab_ana[i].include?(tab_lem[i]) 
        puts tab_ana[i].to_s + " << " + tab_lem[i].to_s
        tp = tp + 1
    else
        fp = fp + 1
    end
    all = all + 1
end
#n - liczba prawidłowych odpowiedzi
puts "n = " + n.to_s
#tp - liczba prawidłowych odpowiedzi, których udzielił system
puts "tp = " + tp.to_s
#fp - liczba nieprawidłowych odpowiedzi, których udzielił system
puts "fp = " + fp.to_s

n = all
# PRECISION
p = tp.to_f / (fp +  tp)
puts "Precision: " + p.to_s
#RACALL
r = tp.to_f/n
puts "Recall: " + r.to_s
#F-MEASURE
f = (2*p.to_f*r)/(r.to_f+p)
puts "F-measure: " + f.to_s

