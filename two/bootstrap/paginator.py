from django.core.paginator import Paginator

class SectionedPaginator(Paginator):
    def sections(self, page, windowsize=6):
        np = self.num_pages

        b = m = e = []

        ##
        ## provide sort of a sliding window over the available
        ## pages with the current page in the center.
        ## windowsize is the size of this window
        if np > windowsize*2:
            b = [1]
            e = [np]
            start = max(3, page - windowsize/2)
            end = start + windowsize+1
            if end > np-2:
                end = np - 1
                start = end - windowsize - 1

            if page < 4:
                b = range(1, windowsize)
                e = [np]
            elif page > (np - 3):
                b = [1]
                e = range(np+1-windowsize, np+1)
            else:
                m = range(start, end)
        else:
            b = range(1, np + 1)

        return b, m, e
