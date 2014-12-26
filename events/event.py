# Event processing module


listeners = [];

def add_event(event_map) :
  for lf in listeners:
    lf(event_map)

def add_event_listener(listener_function) :
  listeners.append(listener_function)

def remove_event_listener(listener_function) :
  listeners.remove(listener_function)
