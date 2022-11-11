---
layout: container
name:  "quay.io/biocontainers/ctat-metagenomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ctat-metagenomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ctat-metagenomics/container.yaml"
updated_at: "2022-11-11 00:51:06.768919"
latest: "1.0.1--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/ctat-metagenomics"
aliases:
 - "centrifuge"
 - "centrifuge-BuildSharedSequence.pl"
 - "centrifuge-RemoveEmptySequence.pl"
 - "centrifuge-RemoveN.pl"
 - "centrifuge-build"
 - "centrifuge-build-bin"
 - "centrifuge-class"
 - "centrifuge-compress.pl"
 - "centrifuge-download"
 - "centrifuge-inspect"
 - "centrifuge-inspect-bin"
 - "centrifuge-kreport"
 - "centrifuge-sort-nt.pl"
 - "centrifuge_evaluate.py"
 - "centrifuge_simulate_reads.py"
 - "metagenomics"
 - "tar"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
versions:
 - "1.0.1--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for ctat-metagenomics"
config: {"url": "https://biocontainers.pro/tools/ctat-metagenomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ctat-metagenomics", "latest": {"1.0.1--hdfd78af_4": "sha256:69ce538bcc6fd685d8f429720febc4b74cca9ec93516e5a630d555c475495918"}, "tags": {"1.0.1--hdfd78af_4": "sha256:69ce538bcc6fd685d8f429720febc4b74cca9ec93516e5a630d555c475495918"}, "docker": "quay.io/biocontainers/ctat-metagenomics", "aliases": {"centrifuge": "/usr/local/bin/centrifuge", "centrifuge-BuildSharedSequence.pl": "/usr/local/bin/centrifuge-BuildSharedSequence.pl", "centrifuge-RemoveEmptySequence.pl": "/usr/local/bin/centrifuge-RemoveEmptySequence.pl", "centrifuge-RemoveN.pl": "/usr/local/bin/centrifuge-RemoveN.pl", "centrifuge-build": "/usr/local/bin/centrifuge-build", "centrifuge-build-bin": "/usr/local/bin/centrifuge-build-bin", "centrifuge-class": "/usr/local/bin/centrifuge-class", "centrifuge-compress.pl": "/usr/local/bin/centrifuge-compress.pl", "centrifuge-download": "/usr/local/bin/centrifuge-download", "centrifuge-inspect": "/usr/local/bin/centrifuge-inspect", "centrifuge-inspect-bin": "/usr/local/bin/centrifuge-inspect-bin", "centrifuge-kreport": "/usr/local/bin/centrifuge-kreport", "centrifuge-sort-nt.pl": "/usr/local/bin/centrifuge-sort-nt.pl", "centrifuge_evaluate.py": "/usr/local/bin/centrifuge_evaluate.py", "centrifuge_simulate_reads.py": "/usr/local/bin/centrifuge_simulate_reads.py", "metagenomics": "/usr/local/bin/metagenomics", "tar": "/usr/local/bin/tar", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ctat-metagenomics.
shpc-registry automated BioContainers addition for ctat-metagenomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ctat-metagenomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ctat-metagenomics:1.0.1--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ctat-metagenomics/1.0.1--hdfd78af_4
$ module help quay.io/biocontainers/ctat-metagenomics/1.0.1--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ctat-metagenomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ctat-metagenomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ctat-metagenomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ctat-metagenomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ctat-metagenomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ctat-metagenomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centrifuge

```bash
$ singularity exec <container> /usr/local/bin/centrifuge
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-BuildSharedSequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-BuildSharedSequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveEmptySequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveEmptySequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveN.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveN.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-class

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-class
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-compress.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-compress.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-download

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-download
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-kreport

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-kreport
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-sort-nt.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-sort-nt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge_evaluate.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_evaluate.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge_simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagenomics

```bash
$ singularity exec <container> /usr/local/bin/metagenomics
$ podman run --it --rm --entrypoint /usr/local/bin/metagenomics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagenomics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
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