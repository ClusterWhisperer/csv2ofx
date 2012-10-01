<?php

$spec = Pearfarm_PackageSpec::create(
	array(Pearfarm_PackageSpec::OPT_BASEDIR => dirname(__FILE__))
)
	->setName('csv2ofx')
	->setChannel('reubano.pearfarm.org')
	->setSummary('converts csv files to ofx and qif files')
	->setDescription('csv2ofx is a command line program that converts CSV files to OFX and QIF files for importing into GnuCash or similar financial accounting programs. csv2ofx has built in support for importing csv files from mint, yoodle, and xero.')
	->setReleaseVersion('0.9.1')
	->setReleaseStability('beta')
	->setApiVersion('0.9.1')
	->setApiStability('beta')
	->setLicense(Pearfarm_PackageSpec::LICENSE_MIT)
	->setNotes('http://github.com/reubano/csv2ofx')
	->addMaintainer('lead', 'Reuben Cummings', 'reubano', 'reubano@gmail.com')
	->addGitFiles()
	->setDependsOnPHPVersion('5.3')
	->addPackageDependency('Console_CommandLine', 'pear.php.net')
	->addExcludeFiles(array('.gitignore', 'pearfarm.spec', '.gittrees'))
	->addExecutable('csv2ofx.php')
	;