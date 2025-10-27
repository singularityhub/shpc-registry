---
layout: container
name:  "quay.io/biocontainers/tinker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tinker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tinker/container.yaml"
updated_at: "2025-10-27 03:32:48.916944"
latest: "8.11.3--h8d36177_0"
container_url: "https://biocontainers.pro/tools/tinker"
aliases:
 - "alchemy"
 - "analyze"
 - "anneal"
 - "arcedit"
 - "bar"
 - "correlate"
 - "critical"
 - "crystal"
 - "diffuse"
 - "distgeom"
 - "document"
 - "dynamic"
 - "freefix"
 - "gda"
 - "intedit"
 - "intxyz"
 - "minimize"
 - "minirot"
 - "minrigid"
 - "mol2xyz"
 - "molxyz"
 - "monte"
 - "newton"
 - "newtrot"
 - "nucleic"
 - "optimize"
 - "optirot"
 - "optrigid"
 - "path"
 - "pdbxyz"
 - "polarize"
 - "poledit"
 - "potential"
 - "prmedit"
 - "protein"
 - "pss"
 - "pssrigid"
 - "pssrot"
 - "radial"
 - "saddle"
 - "scan"
 - "sniffer"
 - "spacefill"
 - "spectrum"
 - "superpose"
 - "testgrad"
 - "testhess"
 - "testpair"
 - "testpol"
 - "testrot"
 - "testsurf"
 - "testvir"
 - "timer"
 - "timerot"
 - "torsfit"
 - "valence"
 - "vibbig"
 - "vibrate"
 - "vibrot"
 - "xtalfit"
 - "xtalmin"
 - "xyzedit"
 - "xyzint"
 - "xyzmol2"
 - "xyzpdb"
versions:
 - "8.11.3--h8d36177_0"
description: "singularity registry hpc automated addition for tinker"
config: {"url": "https://biocontainers.pro/tools/tinker", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tinker", "latest": {"8.11.3--h8d36177_0": "sha256:de7cef5f4c523818056246abce919d8c6b5f8a1ded48c2c2b03e847a5e4ad38f"}, "tags": {"8.11.3--h8d36177_0": "sha256:de7cef5f4c523818056246abce919d8c6b5f8a1ded48c2c2b03e847a5e4ad38f"}, "docker": "quay.io/biocontainers/tinker", "aliases": {"alchemy": "/usr/local/bin/alchemy", "analyze": "/usr/local/bin/analyze", "anneal": "/usr/local/bin/anneal", "arcedit": "/usr/local/bin/arcedit", "bar": "/usr/local/bin/bar", "correlate": "/usr/local/bin/correlate", "critical": "/usr/local/bin/critical", "crystal": "/usr/local/bin/crystal", "diffuse": "/usr/local/bin/diffuse", "distgeom": "/usr/local/bin/distgeom", "document": "/usr/local/bin/document", "dynamic": "/usr/local/bin/dynamic", "freefix": "/usr/local/bin/freefix", "gda": "/usr/local/bin/gda", "intedit": "/usr/local/bin/intedit", "intxyz": "/usr/local/bin/intxyz", "minimize": "/usr/local/bin/minimize", "minirot": "/usr/local/bin/minirot", "minrigid": "/usr/local/bin/minrigid", "mol2xyz": "/usr/local/bin/mol2xyz", "molxyz": "/usr/local/bin/molxyz", "monte": "/usr/local/bin/monte", "newton": "/usr/local/bin/newton", "newtrot": "/usr/local/bin/newtrot", "nucleic": "/usr/local/bin/nucleic", "optimize": "/usr/local/bin/optimize", "optirot": "/usr/local/bin/optirot", "optrigid": "/usr/local/bin/optrigid", "path": "/usr/local/bin/path", "pdbxyz": "/usr/local/bin/pdbxyz", "polarize": "/usr/local/bin/polarize", "poledit": "/usr/local/bin/poledit", "potential": "/usr/local/bin/potential", "prmedit": "/usr/local/bin/prmedit", "protein": "/usr/local/bin/protein", "pss": "/usr/local/bin/pss", "pssrigid": "/usr/local/bin/pssrigid", "pssrot": "/usr/local/bin/pssrot", "radial": "/usr/local/bin/radial", "saddle": "/usr/local/bin/saddle", "scan": "/usr/local/bin/scan", "sniffer": "/usr/local/bin/sniffer", "spacefill": "/usr/local/bin/spacefill", "spectrum": "/usr/local/bin/spectrum", "superpose": "/usr/local/bin/superpose", "testgrad": "/usr/local/bin/testgrad", "testhess": "/usr/local/bin/testhess", "testpair": "/usr/local/bin/testpair", "testpol": "/usr/local/bin/testpol", "testrot": "/usr/local/bin/testrot", "testsurf": "/usr/local/bin/testsurf", "testvir": "/usr/local/bin/testvir", "timer": "/usr/local/bin/timer", "timerot": "/usr/local/bin/timerot", "torsfit": "/usr/local/bin/torsfit", "valence": "/usr/local/bin/valence", "vibbig": "/usr/local/bin/vibbig", "vibrate": "/usr/local/bin/vibrate", "vibrot": "/usr/local/bin/vibrot", "xtalfit": "/usr/local/bin/xtalfit", "xtalmin": "/usr/local/bin/xtalmin", "xyzedit": "/usr/local/bin/xyzedit", "xyzint": "/usr/local/bin/xyzint", "xyzmol2": "/usr/local/bin/xyzmol2", "xyzpdb": "/usr/local/bin/xyzpdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tinker.
singularity registry hpc automated addition for tinker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tinker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tinker:8.11.3--h8d36177_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tinker/8.11.3--h8d36177_0
$ module help quay.io/biocontainers/tinker/8.11.3--h8d36177_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tinker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tinker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tinker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tinker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tinker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tinker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alchemy

```bash
$ singularity exec <container> /usr/local/bin/alchemy
$ podman run --it --rm --entrypoint /usr/local/bin/alchemy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alchemy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyze

```bash
$ singularity exec <container> /usr/local/bin/analyze
$ podman run --it --rm --entrypoint /usr/local/bin/analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anneal

```bash
$ singularity exec <container> /usr/local/bin/anneal
$ podman run --it --rm --entrypoint /usr/local/bin/anneal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anneal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arcedit

```bash
$ singularity exec <container> /usr/local/bin/arcedit
$ podman run --it --rm --entrypoint /usr/local/bin/arcedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arcedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bar

```bash
$ singularity exec <container> /usr/local/bin/bar
$ podman run --it --rm --entrypoint /usr/local/bin/bar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correlate

```bash
$ singularity exec <container> /usr/local/bin/correlate
$ podman run --it --rm --entrypoint /usr/local/bin/correlate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correlate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### critical

```bash
$ singularity exec <container> /usr/local/bin/critical
$ podman run --it --rm --entrypoint /usr/local/bin/critical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/critical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crystal

```bash
$ singularity exec <container> /usr/local/bin/crystal
$ podman run --it --rm --entrypoint /usr/local/bin/crystal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crystal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diffuse

```bash
$ singularity exec <container> /usr/local/bin/diffuse
$ podman run --it --rm --entrypoint /usr/local/bin/diffuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distgeom

```bash
$ singularity exec <container> /usr/local/bin/distgeom
$ podman run --it --rm --entrypoint /usr/local/bin/distgeom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distgeom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### document

```bash
$ singularity exec <container> /usr/local/bin/document
$ podman run --it --rm --entrypoint /usr/local/bin/document   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/document   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamic

```bash
$ singularity exec <container> /usr/local/bin/dynamic
$ podman run --it --rm --entrypoint /usr/local/bin/dynamic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freefix

```bash
$ singularity exec <container> /usr/local/bin/freefix
$ podman run --it --rm --entrypoint /usr/local/bin/freefix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freefix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gda

```bash
$ singularity exec <container> /usr/local/bin/gda
$ podman run --it --rm --entrypoint /usr/local/bin/gda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intedit

```bash
$ singularity exec <container> /usr/local/bin/intedit
$ podman run --it --rm --entrypoint /usr/local/bin/intedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intxyz

```bash
$ singularity exec <container> /usr/local/bin/intxyz
$ podman run --it --rm --entrypoint /usr/local/bin/intxyz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intxyz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimize

```bash
$ singularity exec <container> /usr/local/bin/minimize
$ podman run --it --rm --entrypoint /usr/local/bin/minimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minirot

```bash
$ singularity exec <container> /usr/local/bin/minirot
$ podman run --it --rm --entrypoint /usr/local/bin/minirot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minirot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minrigid

```bash
$ singularity exec <container> /usr/local/bin/minrigid
$ podman run --it --rm --entrypoint /usr/local/bin/minrigid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minrigid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mol2xyz

```bash
$ singularity exec <container> /usr/local/bin/mol2xyz
$ podman run --it --rm --entrypoint /usr/local/bin/mol2xyz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mol2xyz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### molxyz

```bash
$ singularity exec <container> /usr/local/bin/molxyz
$ podman run --it --rm --entrypoint /usr/local/bin/molxyz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/molxyz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monte

```bash
$ singularity exec <container> /usr/local/bin/monte
$ podman run --it --rm --entrypoint /usr/local/bin/monte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### newton

```bash
$ singularity exec <container> /usr/local/bin/newton
$ podman run --it --rm --entrypoint /usr/local/bin/newton   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newton   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### newtrot

```bash
$ singularity exec <container> /usr/local/bin/newtrot
$ podman run --it --rm --entrypoint /usr/local/bin/newtrot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newtrot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucleic

```bash
$ singularity exec <container> /usr/local/bin/nucleic
$ podman run --it --rm --entrypoint /usr/local/bin/nucleic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucleic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optimize

```bash
$ singularity exec <container> /usr/local/bin/optimize
$ podman run --it --rm --entrypoint /usr/local/bin/optimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optirot

```bash
$ singularity exec <container> /usr/local/bin/optirot
$ podman run --it --rm --entrypoint /usr/local/bin/optirot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optirot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optrigid

```bash
$ singularity exec <container> /usr/local/bin/optrigid
$ podman run --it --rm --entrypoint /usr/local/bin/optrigid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optrigid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### path

```bash
$ singularity exec <container> /usr/local/bin/path
$ podman run --it --rm --entrypoint /usr/local/bin/path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdbxyz

```bash
$ singularity exec <container> /usr/local/bin/pdbxyz
$ podman run --it --rm --entrypoint /usr/local/bin/pdbxyz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdbxyz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### polarize

```bash
$ singularity exec <container> /usr/local/bin/polarize
$ podman run --it --rm --entrypoint /usr/local/bin/polarize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polarize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poledit

```bash
$ singularity exec <container> /usr/local/bin/poledit
$ podman run --it --rm --entrypoint /usr/local/bin/poledit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poledit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### potential

```bash
$ singularity exec <container> /usr/local/bin/potential
$ podman run --it --rm --entrypoint /usr/local/bin/potential   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/potential   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prmedit

```bash
$ singularity exec <container> /usr/local/bin/prmedit
$ podman run --it --rm --entrypoint /usr/local/bin/prmedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prmedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protein

```bash
$ singularity exec <container> /usr/local/bin/protein
$ podman run --it --rm --entrypoint /usr/local/bin/protein   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protein   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pss

```bash
$ singularity exec <container> /usr/local/bin/pss
$ podman run --it --rm --entrypoint /usr/local/bin/pss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pssrigid

```bash
$ singularity exec <container> /usr/local/bin/pssrigid
$ podman run --it --rm --entrypoint /usr/local/bin/pssrigid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pssrigid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pssrot

```bash
$ singularity exec <container> /usr/local/bin/pssrot
$ podman run --it --rm --entrypoint /usr/local/bin/pssrot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pssrot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### radial

```bash
$ singularity exec <container> /usr/local/bin/radial
$ podman run --it --rm --entrypoint /usr/local/bin/radial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/radial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saddle

```bash
$ singularity exec <container> /usr/local/bin/saddle
$ podman run --it --rm --entrypoint /usr/local/bin/saddle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saddle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scan

```bash
$ singularity exec <container> /usr/local/bin/scan
$ podman run --it --rm --entrypoint /usr/local/bin/scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sniffer

```bash
$ singularity exec <container> /usr/local/bin/sniffer
$ podman run --it --rm --entrypoint /usr/local/bin/sniffer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sniffer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spacefill

```bash
$ singularity exec <container> /usr/local/bin/spacefill
$ podman run --it --rm --entrypoint /usr/local/bin/spacefill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spacefill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spectrum

```bash
$ singularity exec <container> /usr/local/bin/spectrum
$ podman run --it --rm --entrypoint /usr/local/bin/spectrum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spectrum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### superpose

```bash
$ singularity exec <container> /usr/local/bin/superpose
$ podman run --it --rm --entrypoint /usr/local/bin/superpose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/superpose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testgrad

```bash
$ singularity exec <container> /usr/local/bin/testgrad
$ podman run --it --rm --entrypoint /usr/local/bin/testgrad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testgrad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testhess

```bash
$ singularity exec <container> /usr/local/bin/testhess
$ podman run --it --rm --entrypoint /usr/local/bin/testhess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testhess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testpair

```bash
$ singularity exec <container> /usr/local/bin/testpair
$ podman run --it --rm --entrypoint /usr/local/bin/testpair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testpair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testpol

```bash
$ singularity exec <container> /usr/local/bin/testpol
$ podman run --it --rm --entrypoint /usr/local/bin/testpol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testpol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testrot

```bash
$ singularity exec <container> /usr/local/bin/testrot
$ podman run --it --rm --entrypoint /usr/local/bin/testrot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testrot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testsurf

```bash
$ singularity exec <container> /usr/local/bin/testsurf
$ podman run --it --rm --entrypoint /usr/local/bin/testsurf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsurf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testvir

```bash
$ singularity exec <container> /usr/local/bin/testvir
$ podman run --it --rm --entrypoint /usr/local/bin/testvir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testvir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timer

```bash
$ singularity exec <container> /usr/local/bin/timer
$ podman run --it --rm --entrypoint /usr/local/bin/timer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timerot

```bash
$ singularity exec <container> /usr/local/bin/timerot
$ podman run --it --rm --entrypoint /usr/local/bin/timerot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timerot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torsfit

```bash
$ singularity exec <container> /usr/local/bin/torsfit
$ podman run --it --rm --entrypoint /usr/local/bin/torsfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torsfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### valence

```bash
$ singularity exec <container> /usr/local/bin/valence
$ podman run --it --rm --entrypoint /usr/local/bin/valence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/valence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vibbig

```bash
$ singularity exec <container> /usr/local/bin/vibbig
$ podman run --it --rm --entrypoint /usr/local/bin/vibbig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vibbig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vibrate

```bash
$ singularity exec <container> /usr/local/bin/vibrate
$ podman run --it --rm --entrypoint /usr/local/bin/vibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vibrot

```bash
$ singularity exec <container> /usr/local/bin/vibrot
$ podman run --it --rm --entrypoint /usr/local/bin/vibrot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vibrot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtalfit

```bash
$ singularity exec <container> /usr/local/bin/xtalfit
$ podman run --it --rm --entrypoint /usr/local/bin/xtalfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtalfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtalmin

```bash
$ singularity exec <container> /usr/local/bin/xtalmin
$ podman run --it --rm --entrypoint /usr/local/bin/xtalmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtalmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyzedit

```bash
$ singularity exec <container> /usr/local/bin/xyzedit
$ podman run --it --rm --entrypoint /usr/local/bin/xyzedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xyzedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyzint

```bash
$ singularity exec <container> /usr/local/bin/xyzint
$ podman run --it --rm --entrypoint /usr/local/bin/xyzint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xyzint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyzmol2

```bash
$ singularity exec <container> /usr/local/bin/xyzmol2
$ podman run --it --rm --entrypoint /usr/local/bin/xyzmol2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xyzmol2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyzpdb

```bash
$ singularity exec <container> /usr/local/bin/xyzpdb
$ podman run --it --rm --entrypoint /usr/local/bin/xyzpdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xyzpdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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