---
layout: container
name:  "quay.io/biocontainers/im-pipelines"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/im-pipelines/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/im-pipelines/container.yaml"
updated_at: "2024-08-27 06:00:08.911712"
latest: "1.1.6--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/im-pipelines"
aliases:
 - "cluster_3d"
 - "cluster_butina"
 - "cluster_butina_matrix"
 - "conformers"
 - "constrained_conf_gen"
 - "featurestein_generate"
 - "featurestein_score"
 - "max_min_picker"
 - "molvs"
 - "o3dAlign"
 - "obabel_prepare_pdb"
 - "pbf_ev"
 - "pk_tmax_cmax_sim"
 - "plip"
 - "prepare_tether"
 - "rxn_maker"
 - "rxn_selector"
 - "rxn_smarts_filter"
 - "sanifier"
 - "screen"
 - "screen_multi"
 - "smog2016"
 - "split_fragnet_candidates"
 - "standardise-mols"
 - "standardiser"
 - "standardize"
 - "sucos"
 - "sucos_max"
 - "xcos"
 - "sample"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "jpgicc"
 - "linkicc"
 - "psicc"
versions:
 - "1.1.6--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for im-pipelines"
config: {"url": "https://biocontainers.pro/tools/im-pipelines", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for im-pipelines", "latest": {"1.1.6--pyh3252c3a_0": "sha256:1ad3e7b7dc9811270716b8237d9cc1497de5bcb3ec46f4f4029d42dc811e489e"}, "tags": {"1.1.6--pyh3252c3a_0": "sha256:1ad3e7b7dc9811270716b8237d9cc1497de5bcb3ec46f4f4029d42dc811e489e"}, "docker": "quay.io/biocontainers/im-pipelines", "aliases": {"cluster_3d": "/usr/local/bin/cluster_3d", "cluster_butina": "/usr/local/bin/cluster_butina", "cluster_butina_matrix": "/usr/local/bin/cluster_butina_matrix", "conformers": "/usr/local/bin/conformers", "constrained_conf_gen": "/usr/local/bin/constrained_conf_gen", "featurestein_generate": "/usr/local/bin/featurestein_generate", "featurestein_score": "/usr/local/bin/featurestein_score", "max_min_picker": "/usr/local/bin/max_min_picker", "molvs": "/usr/local/bin/molvs", "o3dAlign": "/usr/local/bin/o3dAlign", "obabel_prepare_pdb": "/usr/local/bin/obabel_prepare_pdb", "pbf_ev": "/usr/local/bin/pbf_ev", "pk_tmax_cmax_sim": "/usr/local/bin/pk_tmax_cmax_sim", "plip": "/usr/local/bin/plip", "prepare_tether": "/usr/local/bin/prepare_tether", "rxn_maker": "/usr/local/bin/rxn_maker", "rxn_selector": "/usr/local/bin/rxn_selector", "rxn_smarts_filter": "/usr/local/bin/rxn_smarts_filter", "sanifier": "/usr/local/bin/sanifier", "screen": "/usr/local/bin/screen", "screen_multi": "/usr/local/bin/screen_multi", "smog2016": "/usr/local/bin/smog2016", "split_fragnet_candidates": "/usr/local/bin/split_fragnet_candidates", "standardise-mols": "/usr/local/bin/standardise-mols", "standardiser": "/usr/local/bin/standardiser", "standardize": "/usr/local/bin/standardize", "sucos": "/usr/local/bin/sucos", "sucos_max": "/usr/local/bin/sucos_max", "xcos": "/usr/local/bin/xcos", "sample": "/usr/local/bin/sample", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "psicc": "/usr/local/bin/psicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/im-pipelines.
shpc-registry automated BioContainers addition for im-pipelines
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/im-pipelines
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/im-pipelines:1.1.6--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/im-pipelines/1.1.6--pyh3252c3a_0
$ module help quay.io/biocontainers/im-pipelines/1.1.6--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### im-pipelines-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### im-pipelines-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### im-pipelines-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### im-pipelines-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### im-pipelines-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### im-pipelines-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cluster_3d

```bash
$ singularity exec <container> /usr/local/bin/cluster_3d
$ podman run --it --rm --entrypoint /usr/local/bin/cluster_3d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster_3d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster_butina

```bash
$ singularity exec <container> /usr/local/bin/cluster_butina
$ podman run --it --rm --entrypoint /usr/local/bin/cluster_butina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster_butina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster_butina_matrix

```bash
$ singularity exec <container> /usr/local/bin/cluster_butina_matrix
$ podman run --it --rm --entrypoint /usr/local/bin/cluster_butina_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster_butina_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conformers

```bash
$ singularity exec <container> /usr/local/bin/conformers
$ podman run --it --rm --entrypoint /usr/local/bin/conformers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conformers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### constrained_conf_gen

```bash
$ singularity exec <container> /usr/local/bin/constrained_conf_gen
$ podman run --it --rm --entrypoint /usr/local/bin/constrained_conf_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/constrained_conf_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featurestein_generate

```bash
$ singularity exec <container> /usr/local/bin/featurestein_generate
$ podman run --it --rm --entrypoint /usr/local/bin/featurestein_generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featurestein_generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featurestein_score

```bash
$ singularity exec <container> /usr/local/bin/featurestein_score
$ podman run --it --rm --entrypoint /usr/local/bin/featurestein_score   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featurestein_score   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### max_min_picker

```bash
$ singularity exec <container> /usr/local/bin/max_min_picker
$ podman run --it --rm --entrypoint /usr/local/bin/max_min_picker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/max_min_picker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### molvs

```bash
$ singularity exec <container> /usr/local/bin/molvs
$ podman run --it --rm --entrypoint /usr/local/bin/molvs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/molvs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### o3dAlign

```bash
$ singularity exec <container> /usr/local/bin/o3dAlign
$ podman run --it --rm --entrypoint /usr/local/bin/o3dAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/o3dAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obabel_prepare_pdb

```bash
$ singularity exec <container> /usr/local/bin/obabel_prepare_pdb
$ podman run --it --rm --entrypoint /usr/local/bin/obabel_prepare_pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obabel_prepare_pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbf_ev

```bash
$ singularity exec <container> /usr/local/bin/pbf_ev
$ podman run --it --rm --entrypoint /usr/local/bin/pbf_ev   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbf_ev   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pk_tmax_cmax_sim

```bash
$ singularity exec <container> /usr/local/bin/pk_tmax_cmax_sim
$ podman run --it --rm --entrypoint /usr/local/bin/pk_tmax_cmax_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pk_tmax_cmax_sim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plip

```bash
$ singularity exec <container> /usr/local/bin/plip
$ podman run --it --rm --entrypoint /usr/local/bin/plip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_tether

```bash
$ singularity exec <container> /usr/local/bin/prepare_tether
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_tether   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_tether   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rxn_maker

```bash
$ singularity exec <container> /usr/local/bin/rxn_maker
$ podman run --it --rm --entrypoint /usr/local/bin/rxn_maker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rxn_maker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rxn_selector

```bash
$ singularity exec <container> /usr/local/bin/rxn_selector
$ podman run --it --rm --entrypoint /usr/local/bin/rxn_selector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rxn_selector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rxn_smarts_filter

```bash
$ singularity exec <container> /usr/local/bin/rxn_smarts_filter
$ podman run --it --rm --entrypoint /usr/local/bin/rxn_smarts_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rxn_smarts_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sanifier

```bash
$ singularity exec <container> /usr/local/bin/sanifier
$ podman run --it --rm --entrypoint /usr/local/bin/sanifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sanifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### screen

```bash
$ singularity exec <container> /usr/local/bin/screen
$ podman run --it --rm --entrypoint /usr/local/bin/screen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/screen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### screen_multi

```bash
$ singularity exec <container> /usr/local/bin/screen_multi
$ podman run --it --rm --entrypoint /usr/local/bin/screen_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/screen_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smog2016

```bash
$ singularity exec <container> /usr/local/bin/smog2016
$ podman run --it --rm --entrypoint /usr/local/bin/smog2016   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smog2016   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_fragnet_candidates

```bash
$ singularity exec <container> /usr/local/bin/split_fragnet_candidates
$ podman run --it --rm --entrypoint /usr/local/bin/split_fragnet_candidates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_fragnet_candidates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### standardise-mols

```bash
$ singularity exec <container> /usr/local/bin/standardise-mols
$ podman run --it --rm --entrypoint /usr/local/bin/standardise-mols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/standardise-mols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### standardiser

```bash
$ singularity exec <container> /usr/local/bin/standardiser
$ podman run --it --rm --entrypoint /usr/local/bin/standardiser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/standardiser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### standardize

```bash
$ singularity exec <container> /usr/local/bin/standardize
$ podman run --it --rm --entrypoint /usr/local/bin/standardize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/standardize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sucos

```bash
$ singularity exec <container> /usr/local/bin/sucos
$ podman run --it --rm --entrypoint /usr/local/bin/sucos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sucos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sucos_max

```bash
$ singularity exec <container> /usr/local/bin/sucos_max
$ podman run --it --rm --entrypoint /usr/local/bin/sucos_max   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sucos_max   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcos

```bash
$ singularity exec <container> /usr/local/bin/xcos
$ podman run --it --rm --entrypoint /usr/local/bin/xcos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample

```bash
$ singularity exec <container> /usr/local/bin/sample
$ podman run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
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