---
layout: container
name:  "quay.io/biocontainers/chemproflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chemproflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chemproflow/container.yaml"
updated_at: "2026-09-02 06:56:46.847575"
latest: "1.2.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/chemproflow"
aliases:
 - "chemproflow"
 - "fabric"
 - "optuna"
 - "sparqlquery"
 - "community"
 - "alembic"
 - "xxh3sum"
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "mako-render"
 - "protoc-33.5.0"
 - "protoc-gen-upb-33.5.0"
 - "protoc-gen-upb_minitable-33.5.0"
 - "protoc-gen-upbdefs-33.5.0"
 - "idna"
 - "fc-genconf"
 - "torchfrtrace"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
 - "ldapurl"
versions:
 - "1.2.0--pyh106432d_0"
description: "singularity registry hpc automated addition for chemproflow"
config: {"url": "https://biocontainers.pro/tools/chemproflow", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for chemproflow", "latest": {"1.2.0--pyh106432d_0": "sha256:8f4f76ac6eaf8d6be13e15a278acfba9f4e327b4e6ab2216bea617c340efe86c"}, "tags": {"1.2.0--pyh106432d_0": "sha256:8f4f76ac6eaf8d6be13e15a278acfba9f4e327b4e6ab2216bea617c340efe86c"}, "docker": "quay.io/biocontainers/chemproflow", "aliases": {"chemproflow": "/usr/local/bin/chemproflow", "fabric": "/usr/local/bin/fabric", "optuna": "/usr/local/bin/optuna", "sparqlquery": "/usr/local/bin/sparqlquery", "community": "/usr/local/bin/community", "alembic": "/usr/local/bin/alembic", "xxh3sum": "/usr/local/bin/xxh3sum", "csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "mako-render": "/usr/local/bin/mako-render", "protoc-33.5.0": "/usr/local/bin/protoc-33.5.0", "protoc-gen-upb-33.5.0": "/usr/local/bin/protoc-gen-upb-33.5.0", "protoc-gen-upb_minitable-33.5.0": "/usr/local/bin/protoc-gen-upb_minitable-33.5.0", "protoc-gen-upbdefs-33.5.0": "/usr/local/bin/protoc-gen-upbdefs-33.5.0", "idna": "/usr/local/bin/idna", "fc-genconf": "/usr/local/bin/fc-genconf", "torchfrtrace": "/usr/local/bin/torchfrtrace", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chemproflow.
singularity registry hpc automated addition for chemproflow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chemproflow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chemproflow:1.2.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chemproflow/1.2.0--pyh106432d_0
$ module help quay.io/biocontainers/chemproflow/1.2.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chemproflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chemproflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chemproflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chemproflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chemproflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chemproflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chemproflow

```bash
$ singularity exec <container> /usr/local/bin/chemproflow
$ podman run --it --rm --entrypoint /usr/local/bin/chemproflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chemproflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fabric

```bash
$ singularity exec <container> /usr/local/bin/fabric
$ podman run --it --rm --entrypoint /usr/local/bin/fabric   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fabric   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optuna

```bash
$ singularity exec <container> /usr/local/bin/optuna
$ podman run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sparqlquery

```bash
$ singularity exec <container> /usr/local/bin/sparqlquery
$ podman run --it --rm --entrypoint /usr/local/bin/sparqlquery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sparqlquery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### community

```bash
$ singularity exec <container> /usr/local/bin/community
$ podman run --it --rm --entrypoint /usr/local/bin/community   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/community   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alembic

```bash
$ singularity exec <container> /usr/local/bin/alembic
$ podman run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapadd

```bash
$ singularity exec <container> /usr/local/bin/ldapadd
$ podman run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapcompare

```bash
$ singularity exec <container> /usr/local/bin/ldapcompare
$ podman run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapdelete

```bash
$ singularity exec <container> /usr/local/bin/ldapdelete
$ podman run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapexop

```bash
$ singularity exec <container> /usr/local/bin/ldapexop
$ podman run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodify

```bash
$ singularity exec <container> /usr/local/bin/ldapmodify
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodrdn

```bash
$ singularity exec <container> /usr/local/bin/ldapmodrdn
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldappasswd

```bash
$ singularity exec <container> /usr/local/bin/ldappasswd
$ podman run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapsearch

```bash
$ singularity exec <container> /usr/local/bin/ldapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapurl

```bash
$ singularity exec <container> /usr/local/bin/ldapurl
$ podman run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
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