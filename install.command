echo "installing..."
cd ~/
rm ".zshrc"
curl -o ".zshrc" "https://raw.githubusercontent.com/furbyboom/furbyiscutestofall/main/thing.sh"
cd ~
rm "tools"
curl -o "tools" "https://raw.githubusercontent.com/furbyboom/furbyiscutestofall/main/tools.command"
echo "done installing..."
