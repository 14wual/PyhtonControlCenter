#!/usr/bin/sh

dir="$HOME/.config/pcc"

launch() {
	python3 $HOME/.config/pcc/options/$section/pcc.py
}

if [[ "$1" == '-a' ]]; then
	section="all"
	launch
elif [[ "$1" == '--all' ]]; then
	section="all"
	launch
elif [[ "$1" == '--wifi' ]]; then
	section="wifi"
	launch
elif [[ "$1" == '--bluetooth' ]]; then
	section="bluetooth"
	launch
elif [[ "$1" == '--brightness' ]]; then
	section="brightness"
	launch
elif [[ "$1" == '--sound' ]]; then
	section="sound"
	launch
elif [[ "$1" == '--lock' ]]; then
	section="lock"
	launch
elif [[ "$1" == '--status' ]]; then
	section="status"
	launch
elif [[ "$1" == '--settings' ]]; then
	section="settings"
	launch
else
	cat <<- EOF
	Usage : ./pcc --option
		
	Available Options :
	--all		--wifi		--lock			-a
	--help		--bluetooth     --status		-h
	--audio		--brightness    --settings
	EOF
fi
