---
layout: container
name:  "quay.io/biocontainers/odamnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/odamnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/odamnet/container.yaml"
updated_at: "2024-03-29 02:58:30.570156"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/odamnet"
aliases:
 - "odamnet"
 - "rqw"
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "rst2html4.py"
 - "rst2html5.py"
 - "rst2html.py"
 - "rst2latex.py"
 - "rst2man.py"
 - "rst2odt.py"
 - "rst2odt_prepstyles.py"
 - "rst2pseudoxml.py"
 - "rst2s5.py"
 - "rst2xetex.py"
 - "rst2xml.py"
 - "rstpep2html.py"
 - "brotli"
 - "normalizer"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for odamnet"
config: {"url": "https://biocontainers.pro/tools/odamnet", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for odamnet", "latest": {"1.1.0--pyhdfd78af_0": "sha256:65e50cbcc2e630283ddc25f6eb1d7e63aa510ec22752993b929c76554d749798"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:65e50cbcc2e630283ddc25f6eb1d7e63aa510ec22752993b929c76554d749798"}, "docker": "quay.io/biocontainers/odamnet", "aliases": {"odamnet": "/usr/local/bin/odamnet", "rqw": "/usr/local/bin/rqw", "csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py", "rst2latex.py": "/usr/local/bin/rst2latex.py", "rst2man.py": "/usr/local/bin/rst2man.py", "rst2odt.py": "/usr/local/bin/rst2odt.py", "rst2odt_prepstyles.py": "/usr/local/bin/rst2odt_prepstyles.py", "rst2pseudoxml.py": "/usr/local/bin/rst2pseudoxml.py", "rst2s5.py": "/usr/local/bin/rst2s5.py", "rst2xetex.py": "/usr/local/bin/rst2xetex.py", "rst2xml.py": "/usr/local/bin/rst2xml.py", "rstpep2html.py": "/usr/local/bin/rstpep2html.py", "brotli": "/usr/local/bin/brotli", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/odamnet.
singularity registry hpc automated addition for odamnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/odamnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/odamnet:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/odamnet/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/odamnet/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### odamnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### odamnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### odamnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### odamnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### odamnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### odamnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### odamnet

```bash
$ singularity exec <container> /usr/local/bin/odamnet
$ podman run --it --rm --entrypoint /usr/local/bin/odamnet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odamnet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rqw

```bash
$ singularity exec <container> /usr/local/bin/rqw
$ podman run --it --rm --entrypoint /usr/local/bin/rqw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rqw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdf2dot

```bash
$ singularity exec <container> /usr/local/bin/rdf2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfgraphisomorphism

```bash
$ singularity exec <container> /usr/local/bin/rdfgraphisomorphism
$ podman run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfpipe

```bash
$ singularity exec <container> /usr/local/bin/rdfpipe
$ podman run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfs2dot

```bash
$ singularity exec <container> /usr/local/bin/rdfs2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex.py

```bash
$ singularity exec <container> /usr/local/bin/rst2latex.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man.py

```bash
$ singularity exec <container> /usr/local/bin/rst2man.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt_prepstyles.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt_prepstyles.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml.py

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2s5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex.py

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml.py

```bash
$ singularity exec <container> /usr/local/bin/rst2xml.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rstpep2html.py

```bash
$ singularity exec <container> /usr/local/bin/rstpep2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rstpep2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rstpep2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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