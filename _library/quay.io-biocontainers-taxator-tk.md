---
layout: container
name:  "quay.io/biocontainers/taxator-tk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taxator-tk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/taxator-tk/container.yaml"
updated_at: "2024-11-18 03:42:55.066625"
latest: "1.3.3e--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/taxator-tk"
aliases:
 - "alignments-filter"
 - "binner"
 - "fasta-strip-identifier"
 - "last-merge-batches"
 - "last_maf_convert.py"
 - "taxator"
 - "taxatortk.py"
 - "taxknife"
 - "taxsummary2krona"
 - "f2py2"
 - "f2py2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.3.3e--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for taxator-tk"
config: {"url": "https://biocontainers.pro/tools/taxator-tk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taxator-tk", "latest": {"1.3.3e--hdfd78af_2": "sha256:afdb530ec60bbd93136309967fb504194cb6c96bbb587f477a163b6412673688"}, "tags": {"1.3.3e--hdfd78af_2": "sha256:afdb530ec60bbd93136309967fb504194cb6c96bbb587f477a163b6412673688"}, "docker": "quay.io/biocontainers/taxator-tk", "aliases": {"alignments-filter": "/usr/local/bin/alignments-filter", "binner": "/usr/local/bin/binner", "fasta-strip-identifier": "/usr/local/bin/fasta-strip-identifier", "last-merge-batches": "/usr/local/bin/last-merge-batches", "last_maf_convert.py": "/usr/local/bin/last_maf_convert.py", "taxator": "/usr/local/bin/taxator", "taxatortk.py": "/usr/local/bin/taxatortk.py", "taxknife": "/usr/local/bin/taxknife", "taxsummary2krona": "/usr/local/bin/taxsummary2krona", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taxator-tk.
shpc-registry automated BioContainers addition for taxator-tk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taxator-tk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taxator-tk:1.3.3e--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taxator-tk/1.3.3e--hdfd78af_2
$ module help quay.io/biocontainers/taxator-tk/1.3.3e--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taxator-tk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taxator-tk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taxator-tk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taxator-tk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taxator-tk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taxator-tk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alignments-filter

```bash
$ singularity exec <container> /usr/local/bin/alignments-filter
$ podman run --it --rm --entrypoint /usr/local/bin/alignments-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignments-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binner

```bash
$ singularity exec <container> /usr/local/bin/binner
$ podman run --it --rm --entrypoint /usr/local/bin/binner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-strip-identifier

```bash
$ singularity exec <container> /usr/local/bin/fasta-strip-identifier
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-strip-identifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-strip-identifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-merge-batches

```bash
$ singularity exec <container> /usr/local/bin/last-merge-batches
$ podman run --it --rm --entrypoint /usr/local/bin/last-merge-batches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-merge-batches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last_maf_convert.py

```bash
$ singularity exec <container> /usr/local/bin/last_maf_convert.py
$ podman run --it --rm --entrypoint /usr/local/bin/last_maf_convert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last_maf_convert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxator

```bash
$ singularity exec <container> /usr/local/bin/taxator
$ podman run --it --rm --entrypoint /usr/local/bin/taxator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxatortk.py

```bash
$ singularity exec <container> /usr/local/bin/taxatortk.py
$ podman run --it --rm --entrypoint /usr/local/bin/taxatortk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxatortk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxknife

```bash
$ singularity exec <container> /usr/local/bin/taxknife
$ podman run --it --rm --entrypoint /usr/local/bin/taxknife   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxknife   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxsummary2krona

```bash
$ singularity exec <container> /usr/local/bin/taxsummary2krona
$ podman run --it --rm --entrypoint /usr/local/bin/taxsummary2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxsummary2krona   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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