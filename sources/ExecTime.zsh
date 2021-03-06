# Function executed before every command run by the shell
function pbt_exectime_pre() {
    export PBT_CAR_EXECTIME_SECS=$(date '+%s.%N')
    PBT_CAR_EXECTIME__TMP=1
}

# Function executed after every command run by the shell
function pbt_exectime_post() {
    if [ -z $PBT_CAR_EXECTIME__TMP ]; then
        export PBT_CAR_EXECTIME_SECS=$(date '+%s.%N')
    else
        # This "else" part is only necessary if you want to ring the system
        # bell if the command is taking more that PBT_CAR_EXECTIME_BELL
        # seconds.
        local BELL=${PBT_CAR_EXECTIME_BELL:-0}

        if (( $BELL > 0 )); then
            local EXECS=$(echo "$(date '+%s.%N') - $PBT_CAR_EXECTIME_SECS" | bc)

            if (( $EXECS > $BELL )); then
                echo -en '\a'
            fi
        fi
    fi

    unset PBT_CAR_EXECTIME__TMP
}

preexec_functions+=(pbt_exectime_pre)
precmd_functions+=(pbt_exectime_post)
