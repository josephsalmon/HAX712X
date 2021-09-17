# Accéder à la console de vs_code avec Windows (et pouvoir l'utiliser).

## Python dans VsCode

### Etape 1 : localiser anaconda

Dans la console anaconda prompt taper `where python`. Vous obtenez un chemin du type `C:\Users\<nom>\Anaconda3\python.exe ` 
(pour ceux qui n'ont pas le même type de chemin il faut juste localiser où est `Anaconda3`, et vérifier que dans celui que vous avez il y a bien un sous-dossier `Scripts`). Vous n'avez besoin de garder (noter) que la partie jusqu'à `Anaconda3` (inclus).

### Etape 2 : enregistrer dans PATH

Chercher (avec Cortana c'est plus simple) `variables d'environnement`. Dans celles du système, double cliquez sur `Path` et faites `Nouveau`. Ajoutez l'adresse que vous aviez noté et enregistrez la. Faites encore une fois `nouveau` et ajoutez la même adresse à laquelle vous rajoutez à la fin `\Scripts\`. Sauvegardez tout.

### Etape 3 : Test

Testez en lançant `vscode` et en tapant python dans la console.

### Etape 4 : (si celles d'avant n'ont pas suffit)

Ouvrir une invite de commande `PowerShell` en administrateur (`powershell` dans Cortana puis click-droit `as admin`). Tapez `set-execution policy unrestricted`. Fermez et refaites l'étape 3


## Sphinx et la reconnaissance du navigateur

Pour afficher facilement la documentation crée avec Sphinx, après avoir fait `make html`, on utilise ```chrome _build/html/index.html```. Pour ceux qui ont une erreur du type "navigateur non reconnu", il faut ajouter le chemin jusqu'à l'executeur de votre navigateur au PATH. C'est-à-dire :

- `C:\Program Files (x86)\Google\Chrome\Application` pour chrome
- `C:\Program Files (x86)\Mozilla Firefox` pour firefox

~~~{.html}
Ce sont (ou ça a été) les chemins normalement mis par défaut lors de l'installation de ces navigateurs. Si vous l'avez changé (volontairement ou pas) recherchez chrome.exe dans Cortana, ouvrez l'emplacement du fichier et copiez l'adresse.
~~~

Ensuite vous n'avez plus qu'à coper le chemin d'accès dans PATH de la même manière qu'à l'étape 2.

### Remarques et liens

On peut utiliser export pour définir de nouvelles variables d'environnement si besoin c'est plus rapide.

Si un jour vous voulez remettre la restriction de l'execution des scripts (on sait jamais) ie annuler l'étape faite avec la powershell, il faudra relancer en mode admin et taper Set-ExecutionPolicy RemoteSigned.

[La powershell autorisation de scripts](http://www.octetmalin.net/windows/scripts/powershell-activer-execution-des-scripts.php)

[Les environnements dans vscode et Windows](https://code.visualstudio.com/docs/python/environments)