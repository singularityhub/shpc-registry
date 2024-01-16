---
layout: container
name:  "quay.io/biocontainers/whatsgnu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/whatsgnu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/whatsgnu/container.yaml"
updated_at: "2024-01-16 02:59:20.800115"
latest: "1.5--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/whatsgnu"
aliases:
 - "Complete_Reference_selector.py"
 - "WhatsGNU_database_customizer.py"
 - "WhatsGNU_get_GenBank_genomes.py"
 - "WhatsGNU_main.py"
 - "WhatsGNU_plotter.py"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
 - "readme.pdf"
versions:
 - "1.3--hdfd78af_0"
 - "1.5--hdfd78af_0"
 - "1.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for whatsgnu"
config: {"url": "https://biocontainers.pro/tools/whatsgnu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for whatsgnu", "latest": {"1.5--hdfd78af_0": "sha256:cb6415f06afa5dcbd1fdd58c56a25945cd2f6d546c0446394e2169f755c4bbb6"}, "tags": {"1.3--hdfd78af_0": "sha256:23accaaaa41fc4610fe982e60af4eda7bcaaf9fb41f935f128e420b729254bd4", "1.5--hdfd78af_0": "sha256:cb6415f06afa5dcbd1fdd58c56a25945cd2f6d546c0446394e2169f755c4bbb6", "1.4--hdfd78af_0": "sha256:3fa85935949e8a2f0263fb43d0f3a6f55538d221c5de69dda54bf7f3ce24ad04"}, "docker": "quay.io/biocontainers/whatsgnu", "aliases": {"Complete_Reference_selector.py": "/usr/local/bin/Complete_Reference_selector.py", "WhatsGNU_database_customizer.py": "/usr/local/bin/WhatsGNU_database_customizer.py", "WhatsGNU_get_GenBank_genomes.py": "/usr/local/bin/WhatsGNU_get_GenBank_genomes.py", "WhatsGNU_main.py": "/usr/local/bin/WhatsGNU_main.py", "WhatsGNU_plotter.py": "/usr/local/bin/WhatsGNU_plotter.py", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect", "readme.pdf": "/usr/local/bin/readme.pdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/whatsgnu.
shpc-registry automated BioContainers addition for whatsgnu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/whatsgnu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/whatsgnu:1.5--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/whatsgnu/1.5--hdfd78af_0
$ module help quay.io/biocontainers/whatsgnu/1.5--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### whatsgnu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### whatsgnu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### whatsgnu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### whatsgnu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### whatsgnu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### whatsgnu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Complete_Reference_selector.py

```bash
$ singularity exec <container> /usr/local/bin/Complete_Reference_selector.py
$ podman run --it --rm --entrypoint /usr/local/bin/Complete_Reference_selector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Complete_Reference_selector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_database_customizer.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_database_customizer.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_database_customizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_database_customizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_get_GenBank_genomes.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_get_GenBank_genomes.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_get_GenBank_genomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_get_GenBank_genomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_main.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_main.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### WhatsGNU_plotter.py

```bash
$ singularity exec <container> /usr/local/bin/WhatsGNU_plotter.py
$ podman run --it --rm --entrypoint /usr/local/bin/WhatsGNU_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WhatsGNU_plotter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readme.pdf

```bash
$ singularity exec <container> /usr/local/bin/readme.pdf
$ podman run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)