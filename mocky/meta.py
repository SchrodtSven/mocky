class Meta:
    
    meta_syntactic = ['bar', 'baz', 'corge', 'eggs', 'foo', 'foobar', 'fred', 'garply', 'grault', 'ham', 'plugh', 'quux', 'qux', 'spam', 'thud', 'waldo', 'xyzzy']
    
    
    def get_meta_syn(self)->list:
        return self.meta_syntactic