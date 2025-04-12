---
layout: container
name:  "quay.io/biocontainers/pyquant-ms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyquant-ms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyquant-ms/container.yaml"
updated_at: "2025-04-12 03:18:48.555071"
latest: "0.2.4--py27h4329609_5"
container_url: "https://biocontainers.pro/tools/pyquant-ms"
aliases:
 - "fastadigest.py"
 - "fastadigeststats.py"
 - "fastxTrimmer.py"
 - "featureCollapser.py"
 - "fetchOrfs.py"
 - "incorporateGFF.py"
 - "incorporateVCF.py"
 - "intersectFiles.py"
 - "junctionalReads.py"
 - "proteinInference.py"
 - "ptmSummary.py"
 - "pyQuant"
 - "f2py2"
 - "f2py2.7"
 - "xslt-config"
 - "xsltproc"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
versions:
 - "0.2.4--py27h4329609_5"
description: "shpc-registry automated BioContainers addition for pyquant-ms"
config: {"url": "https://biocontainers.pro/tools/pyquant-ms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyquant-ms", "latest": {"0.2.4--py27h4329609_5": "sha256:ac6b9c10980b125edd898fc4fed0681a9377c0c3d450686c12a49f087fa5cf41"}, "tags": {"0.2.4--py27h4329609_5": "sha256:ac6b9c10980b125edd898fc4fed0681a9377c0c3d450686c12a49f087fa5cf41"}, "docker": "quay.io/biocontainers/pyquant-ms", "aliases": {"fastadigest.py": "/usr/local/bin/fastadigest.py", "fastadigeststats.py": "/usr/local/bin/fastadigeststats.py", "fastxTrimmer.py": "/usr/local/bin/fastxTrimmer.py", "featureCollapser.py": "/usr/local/bin/featureCollapser.py", "fetchOrfs.py": "/usr/local/bin/fetchOrfs.py", "incorporateGFF.py": "/usr/local/bin/incorporateGFF.py", "incorporateVCF.py": "/usr/local/bin/incorporateVCF.py", "intersectFiles.py": "/usr/local/bin/intersectFiles.py", "junctionalReads.py": "/usr/local/bin/junctionalReads.py", "proteinInference.py": "/usr/local/bin/proteinInference.py", "ptmSummary.py": "/usr/local/bin/ptmSummary.py", "pyQuant": "/usr/local/bin/pyQuant", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyquant-ms.
shpc-registry automated BioContainers addition for pyquant-ms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyquant-ms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyquant-ms:0.2.4--py27h4329609_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyquant-ms/0.2.4--py27h4329609_5
$ module help quay.io/biocontainers/pyquant-ms/0.2.4--py27h4329609_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyquant-ms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyquant-ms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyquant-ms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyquant-ms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyquant-ms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyquant-ms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastadigest.py

```bash
$ singularity exec <container> /usr/local/bin/fastadigest.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastadigest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadigest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastadigeststats.py

```bash
$ singularity exec <container> /usr/local/bin/fastadigeststats.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastadigeststats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadigeststats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastxTrimmer.py

```bash
$ singularity exec <container> /usr/local/bin/fastxTrimmer.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastxTrimmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastxTrimmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featureCollapser.py

```bash
$ singularity exec <container> /usr/local/bin/featureCollapser.py
$ podman run --it --rm --entrypoint /usr/local/bin/featureCollapser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featureCollapser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchOrfs.py

```bash
$ singularity exec <container> /usr/local/bin/fetchOrfs.py
$ podman run --it --rm --entrypoint /usr/local/bin/fetchOrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchOrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### incorporateGFF.py

```bash
$ singularity exec <container> /usr/local/bin/incorporateGFF.py
$ podman run --it --rm --entrypoint /usr/local/bin/incorporateGFF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/incorporateGFF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### incorporateVCF.py

```bash
$ singularity exec <container> /usr/local/bin/incorporateVCF.py
$ podman run --it --rm --entrypoint /usr/local/bin/incorporateVCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/incorporateVCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersectFiles.py

```bash
$ singularity exec <container> /usr/local/bin/intersectFiles.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersectFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersectFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### junctionalReads.py

```bash
$ singularity exec <container> /usr/local/bin/junctionalReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/junctionalReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/junctionalReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinInference.py

```bash
$ singularity exec <container> /usr/local/bin/proteinInference.py
$ podman run --it --rm --entrypoint /usr/local/bin/proteinInference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinInference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptmSummary.py

```bash
$ singularity exec <container> /usr/local/bin/ptmSummary.py
$ podman run --it --rm --entrypoint /usr/local/bin/ptmSummary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptmSummary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyQuant

```bash
$ singularity exec <container> /usr/local/bin/pyQuant
$ podman run --it --rm --entrypoint /usr/local/bin/pyQuant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyQuant   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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