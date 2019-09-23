setup:
1) installare gnu radio
	https://wiki.analog.com/resources/tools-software/linux-software/gnuradio
2) scaricare cartella del progetto 
	git clone https://fdegiudici@bitbucket.org/urgensat/urgensat_app.git
3) creare venv nella cartella urgensat_app/urgensat 
	https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
4) attivare VENV e installare librerie necessarie con pip
	source venv/bin/activate
	pip install -r ../requirements.txt
5) eliminare .example dal file di config dei logger

utilizzo:
1) recarsi nella cartella urgesnat_app/urgensat
2) attivare VENV -> source venv/bin/activate
3) aprire con GRC il flowgraph che si vuole usare e avviarlo
4) avviare le stazione/i

