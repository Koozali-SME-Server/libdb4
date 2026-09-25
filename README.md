# <img src="https://www.koozali.org/images/koozali/Logo/Png/Koozali_logo_2016.png" width="25%" vertical="auto" style="vertical-align:bottom"> libdb4

SMEServer Koozali developed git repo for libdb4 core 

## Wiki
<br />https://wiki.koozali.org/libdb4

## Bugzilla
Show list of outstanding bugs: [here](https://bugs.koozali.org/buglist.cgi?component=libdb4-utils&product=SME%20Server%2011.X&query_format=advanced&limit=0&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=CONFIRMED)

## Description

3rd Party (Maintained by Koozali) git repo for libdb4-utils smeserver

## Note for future 
java is now 17, and it was designed for 1.8 max.
still able to build with a small patch to accept on test 17 and to force 17 to handle as it was 1.8.
in case for el10 it does not work, we could add this in spec

in Requires
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: jpackage-utils

or
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: java-devel < 1:2


in build section
export JAVA_HOME=%{_usr}/lib/jvm/java-1.8.0-openjdk
export PATH=$JAVA_HOME/bin:$PATH

export JAVACFLAGS="-source 1.8 -target 1.8"
