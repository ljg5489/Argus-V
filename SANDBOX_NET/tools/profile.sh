# /etc/profile.d of the internet sandbox (a login shell, `bash -lc`, sets its PATH anew and then reads this).
# pip puts the commands of the packages it installs for the user in ~/.local/bin: found, but after the system's own
# folders, so that nothing written in /workspace can stand in for a program of the image.
case ":$PATH:" in
  *":$HOME/.local/bin:"*) ;;
  *) PATH="$PATH:$HOME/.local/bin"; export PATH ;;
esac
