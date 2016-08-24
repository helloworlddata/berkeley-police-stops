require 'pathname'
DATA_DIR = Pathname 'data'
WRANGLE_DIR = Pathname 'wrangle'
CORRAL_DIR = WRANGLE_DIR.join('corral')
SCRIPTS_DIR = WRANGLE_DIR.join('scripts')
DIRS = {
    'fetched' => CORRAL_DIR.join('fetched'),
    'cleaned' => CORRAL_DIR.join('cleaned'),
    'published' => DATA_DIR,
}

FILES = {
    'fetched' => DIRS['fetched'] / 'berkeley-police-stops.csv',
    'cleaned' => DIRS['cleaned'] / 'berkeley-police-stops.csv',

}


desc 'Setup the directories'
task :setup do
    DIRS.each_value do |p|
        unless p.exist?
            p.mkpath()
            puts "Created directory: #{p}"
        end
    end
end


namespace :publish do
    desc 'got to fetch them all'
    task :fetch => :setup do
        Rake::Task[FILES['fetched']].execute()
    end

    task :clean do
        Rake::Task[FILES['cleaned']].execute()
    end
end



namespace :filings do
    desc "clean up the headers"
    file FILES['cleaned'] => FILES['fetched'] do
        sh "python #{SCRIPTS_DIR / 'clean.py'} #{FILES['fetched']} > #{FILES['cleaned']}"
    end

    file FILES['fetched'] => :setup do
        # meh this doesn't need a script
        src_url = 'https://data.cityofberkeley.info/api/views/6e9j-pj9p/rows.csv?accessType=DOWNLOAD'
        sh "curl #{src_url} -o #{FILES['fetched']}"
    end
end
