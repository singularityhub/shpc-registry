---
layout: container
name:  "quay.io/biocontainers/pm4ngs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pm4ngs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pm4ngs/container.yaml"
updated_at: "2025-09-05 03:32:07.611337"
latest: "0.0.21--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pm4ngs"
aliases:
 - "bagit.py"
 - "bioconda2biocontainer"
 - "bioconda2cwldocker"
 - "biocontainers-search"
 - "cheetah"
 - "cheetah-analyze"
 - "cheetah-compile"
 - "cookiecutter"
 - "galaxy-tool-test"
 - "goenrichment"
 - "jupyter-console"
 - "jupyter-qtconsole"
 - "mulled-build"
 - "mulled-build-channel"
 - "mulled-build-files"
 - "mulled-build-tool"
 - "mulled-list"
 - "mulled-search"
 - "mulled-update-singularity-containers"
 - "pm4ngs-chipexo"
 - "pm4ngs-chipexo-demo"
 - "pm4ngs-chipseq"
 - "pm4ngs-chipseq-demo"
 - "pm4ngs-create"
 - "pm4ngs-rnaseq"
 - "pm4ngs-rnaseq-demo"
 - "pm4ngs-server"
 - "prov-compare"
 - "prov-convert"
 - "wsdump.py"
 - "cwltool"
 - "conda-env"
 - "cph"
 - "schema-salad-doc"
 - "schema-salad-tool"
 - "pdfattach"
 - "csv2rdf"
 - "pdfdetach"
 - "pdffonts"
 - "pdfimages"
versions:
 - "0.0.9--pyhdfd78af_0"
 - "0.0.21--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pm4ngs"
config: {"url": "https://biocontainers.pro/tools/pm4ngs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pm4ngs", "latest": {"0.0.21--pyhdfd78af_0": "sha256:465239c61f4b0249a67062fe075d8943c6f598b62505667e541e6f72fa253fc5"}, "tags": {"0.0.9--pyhdfd78af_0": "sha256:8cc50f6f2bf525f2765f3546d311a1fff1b0009972a9ef0bb951bc8eaecc08e1", "0.0.21--pyhdfd78af_0": "sha256:465239c61f4b0249a67062fe075d8943c6f598b62505667e541e6f72fa253fc5"}, "docker": "quay.io/biocontainers/pm4ngs", "aliases": {"bagit.py": "/usr/local/bin/bagit.py", "bioconda2biocontainer": "/usr/local/bin/bioconda2biocontainer", "bioconda2cwldocker": "/usr/local/bin/bioconda2cwldocker", "biocontainers-search": "/usr/local/bin/biocontainers-search", "cheetah": "/usr/local/bin/cheetah", "cheetah-analyze": "/usr/local/bin/cheetah-analyze", "cheetah-compile": "/usr/local/bin/cheetah-compile", "cookiecutter": "/usr/local/bin/cookiecutter", "galaxy-tool-test": "/usr/local/bin/galaxy-tool-test", "goenrichment": "/usr/local/bin/goenrichment", "jupyter-console": "/usr/local/bin/jupyter-console", "jupyter-qtconsole": "/usr/local/bin/jupyter-qtconsole", "mulled-build": "/usr/local/bin/mulled-build", "mulled-build-channel": "/usr/local/bin/mulled-build-channel", "mulled-build-files": "/usr/local/bin/mulled-build-files", "mulled-build-tool": "/usr/local/bin/mulled-build-tool", "mulled-list": "/usr/local/bin/mulled-list", "mulled-search": "/usr/local/bin/mulled-search", "mulled-update-singularity-containers": "/usr/local/bin/mulled-update-singularity-containers", "pm4ngs-chipexo": "/usr/local/bin/pm4ngs-chipexo", "pm4ngs-chipexo-demo": "/usr/local/bin/pm4ngs-chipexo-demo", "pm4ngs-chipseq": "/usr/local/bin/pm4ngs-chipseq", "pm4ngs-chipseq-demo": "/usr/local/bin/pm4ngs-chipseq-demo", "pm4ngs-create": "/usr/local/bin/pm4ngs-create", "pm4ngs-rnaseq": "/usr/local/bin/pm4ngs-rnaseq", "pm4ngs-rnaseq-demo": "/usr/local/bin/pm4ngs-rnaseq-demo", "pm4ngs-server": "/usr/local/bin/pm4ngs-server", "prov-compare": "/usr/local/bin/prov-compare", "prov-convert": "/usr/local/bin/prov-convert", "wsdump.py": "/usr/local/bin/wsdump.py", "cwltool": "/usr/local/bin/cwltool", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "schema-salad-doc": "/usr/local/bin/schema-salad-doc", "schema-salad-tool": "/usr/local/bin/schema-salad-tool", "pdfattach": "/usr/local/bin/pdfattach", "csv2rdf": "/usr/local/bin/csv2rdf", "pdfdetach": "/usr/local/bin/pdfdetach", "pdffonts": "/usr/local/bin/pdffonts", "pdfimages": "/usr/local/bin/pdfimages"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pm4ngs.
shpc-registry automated BioContainers addition for pm4ngs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pm4ngs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pm4ngs:0.0.21--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pm4ngs/0.0.21--pyhdfd78af_0
$ module help quay.io/biocontainers/pm4ngs/0.0.21--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pm4ngs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pm4ngs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pm4ngs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pm4ngs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pm4ngs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pm4ngs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bagit.py

```bash
$ singularity exec <container> /usr/local/bin/bagit.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconda2biocontainer

```bash
$ singularity exec <container> /usr/local/bin/bioconda2biocontainer
$ podman run --it --rm --entrypoint /usr/local/bin/bioconda2biocontainer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconda2biocontainer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconda2cwldocker

```bash
$ singularity exec <container> /usr/local/bin/bioconda2cwldocker
$ podman run --it --rm --entrypoint /usr/local/bin/bioconda2cwldocker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconda2cwldocker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biocontainers-search

```bash
$ singularity exec <container> /usr/local/bin/biocontainers-search
$ podman run --it --rm --entrypoint /usr/local/bin/biocontainers-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biocontainers-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah

```bash
$ singularity exec <container> /usr/local/bin/cheetah
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-analyze

```bash
$ singularity exec <container> /usr/local/bin/cheetah-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-compile

```bash
$ singularity exec <container> /usr/local/bin/cheetah-compile
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cookiecutter

```bash
$ singularity exec <container> /usr/local/bin/cookiecutter
$ podman run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-tool-test

```bash
$ singularity exec <container> /usr/local/bin/galaxy-tool-test
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### goenrichment

```bash
$ singularity exec <container> /usr/local/bin/goenrichment
$ podman run --it --rm --entrypoint /usr/local/bin/goenrichment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/goenrichment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-qtconsole

```bash
$ singularity exec <container> /usr/local/bin/jupyter-qtconsole
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build

```bash
$ singularity exec <container> /usr/local/bin/mulled-build
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-channel

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-channel
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-files

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-files
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-tool

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-tool
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-list

```bash
$ singularity exec <container> /usr/local/bin/mulled-list
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-search

```bash
$ singularity exec <container> /usr/local/bin/mulled-search
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-update-singularity-containers

```bash
$ singularity exec <container> /usr/local/bin/mulled-update-singularity-containers
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-chipexo

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-chipexo
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipexo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipexo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-chipexo-demo

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-chipexo-demo
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipexo-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipexo-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-chipseq

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-chipseq
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-chipseq-demo

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-chipseq-demo
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipseq-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-chipseq-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-create

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-create
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-rnaseq

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-rnaseq
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-rnaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-rnaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-rnaseq-demo

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-rnaseq-demo
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-rnaseq-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-rnaseq-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm4ngs-server

```bash
$ singularity exec <container> /usr/local/bin/pm4ngs-server
$ podman run --it --rm --entrypoint /usr/local/bin/pm4ngs-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm4ngs-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prov-compare

```bash
$ singularity exec <container> /usr/local/bin/prov-compare
$ podman run --it --rm --entrypoint /usr/local/bin/prov-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prov-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prov-convert

```bash
$ singularity exec <container> /usr/local/bin/prov-convert
$ podman run --it --rm --entrypoint /usr/local/bin/prov-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prov-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump.py

```bash
$ singularity exec <container> /usr/local/bin/wsdump.py
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwltool

```bash
$ singularity exec <container> /usr/local/bin/cwltool
$ podman run --it --rm --entrypoint /usr/local/bin/cwltool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-env

```bash
$ singularity exec <container> /usr/local/bin/conda-env
$ podman run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schema-salad-doc

```bash
$ singularity exec <container> /usr/local/bin/schema-salad-doc
$ podman run --it --rm --entrypoint /usr/local/bin/schema-salad-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schema-salad-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schema-salad-tool

```bash
$ singularity exec <container> /usr/local/bin/schema-salad-tool
$ podman run --it --rm --entrypoint /usr/local/bin/schema-salad-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schema-salad-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfattach

```bash
$ singularity exec <container> /usr/local/bin/pdfattach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfdetach

```bash
$ singularity exec <container> /usr/local/bin/pdfdetach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdffonts

```bash
$ singularity exec <container> /usr/local/bin/pdffonts
$ podman run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfimages

```bash
$ singularity exec <container> /usr/local/bin/pdfimages
$ podman run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
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