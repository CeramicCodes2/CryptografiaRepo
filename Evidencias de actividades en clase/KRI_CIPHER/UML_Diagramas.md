# En esta seccion se presentan los diagramas que conforman los diferentes componentes del sistema

archivo: `kri_cipher.py`

```
classDiagram
    class Encrypt {
        <<abstract>>
        +encrypt(m)
    }

    class Decrypt {
        <<abstract>>
        +decrypt(m)
    }

    class Template {
        <<interface>>
        +Template(input, output)
        +main(input, output)
        +generateKey()
        +input()
        +output(*args)
        +configurations(input, output)
    }

    class Observer {
        <<abstract>>
        +update(subject)
    }

    class Subject {
        <<abstract>>
        +state
        +suscribe(observer: Observer)
        +unsuscribe(observer: Observer)
        +notify()
    }

    class State~T~ {
        +value
        +isPresent()
    }

    class EventObservableHandler {
        +state: State
        +suscribe(observer: Observer)
        +unsuscribe(observer: Observer)
        +notify()
    }

    class Input {
        +Input(handler: EventObservableHandler, state: State~dict~)
        +print(**kwargs)
    }

    class Output {
        +Output(handler: EventObservableHandler, state: State~dict~)
        +output(**kwargs)
    }


    Subject <|-- EventObservableHandler
    State <|-- EventObservableHandler
    EventObservableHandler *-- Input
    EventObservableHandler *-- Output
    State *-- Input
    State *-- Output
    Observer ..> Subject

```


# DiffHellman

```
classDiagram
    class Template {
        +generateKey()
        +input()
        +output(*args)
        +configurations(input, output)
    }

    class Encrypt {
        +encrypt(m)
    }

    class Input {
        +print(**kwargs)
    }

    class KeysContainer {
    }

    class DiffHellman {
        +generateKey()
        +input()
        +validateKey(cp, p)
        +output(*args)
        +encrypt(m)
        +configurations(input, output)
        +generateKeySession(yb, cp, p)
        +generatePublicKey(a, cp, p)
        +generatePrimitiveRoots(p)
        +is_generator(g, p)
    }
    class Input {
        +Input(handler: EventObservableHandler, state: State~dict~)
        +print(**kwargs)
    }

    class Output {
        +Output(handler: EventObservableHandler, state: State~dict~)
        +output(**kwargs)
    }
    class KeysContainer {
        +int cp = 0
        +int cu = 0
        +int yb = 0
        +int channelKey = 0
        +__str__()
        +export()
    }


    Template <|-- DiffHellman
    Encrypt <|-- DiffHellman
    Input <.. DiffHellman
    Output <.. DiffHellman
    KeysContainer <.. DiffHellman
```